import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from moderation.models import BlockingReason

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def setup_reasons():
    reason1 = BlockingReason.objects.create(title="Fotoğraf net değil", hard_block=False, is_active=True)
    reason2 = BlockingReason.objects.create(title="Yasaklı madde", hard_block=True, is_active=True)
    reason3 = BlockingReason.objects.create(title="Eski kural (Pasif)", hard_block=False, is_active=False)
    return reason1, reason2, reason3

@pytest.mark.django_db
def test_list_returns_active_reasons(api_client, setup_reasons):
    # url name moderation/urls.py dosyasındaki name ile eşleşmeli
    url = reverse('product-blocking-reasons') 
    response = api_client.get(url)
    
    assert response.status_code == 200
    # 3 kayıttan sadece 2'si aktif, bu yüzden 2 dönmeli
    assert len(response.data) == 2 
    
    # Doğru alanların gelip gelmediğini (is_active'in sızmadığını) kontrol et
    for item in response.data:
        assert 'id' in item
        assert 'title' in item
        assert 'hard_block' in item
        assert 'is_active' not in item

@pytest.mark.django_db
def test_inactive_reasons_not_visible(api_client, setup_reasons):
    url = reverse('product-blocking-reasons')
    response = api_client.get(url)
    
    # Gelen verilerin başlıklarını bir listeye al
    titles = [item['title'] for item in response.data]
    
    # Pasif olan kaydın başlığı listede KESİNLİKLE olmamalı
    assert "Eski kural (Pasif)" not in titles

@pytest.mark.django_db
def test_referenced_reason_cannot_be_deleted(setup_reasons):
    reason1, _, _ = setup_reasons
    
    # Silme komutunu veriyoruz
    reason1.delete()
    
    # Veritabanından objeyi tazeleyip durumunu kontrol ediyoruz
    reason1.refresh_from_db()
    
    # Veri fiziksel olarak silinmemiş olmalı (id'si hala var olmalı)
    assert reason1.id is not None
    # Ama is_active alanı False'a dönmüş olmalı
    assert reason1.is_active is False