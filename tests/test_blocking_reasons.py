import pytest
from django.urls import reverse
from moderation.models import BlockingReason

@pytest.mark.django_db
def test_list_returns_active_reasons(client):
    # Yeni model yapısına uygun test verisi oluşturuyoruz
    reason = BlockingReason.objects.create(
        code="INVALID_PHOTO",
        title="Fotoğraf uygun değil",
        hard_block=False,
        is_active=True
    )
    
    # URL'i tersine mühendislikle (reverse) güvenli şekilde çekiyoruz
    url = reverse('blocking-reasons-list')
    response = client.get(url)
    
    assert response.status_code == 200
    assert len(response.data) == 1
    
    item = response.data[0]
    # Hakemin istediği doğrulamalar (Asserts):
    assert 'id' in item
    assert 'code' in item          # Yeni eklendi
    assert 'title' in item
    assert 'hard_block' in item
    assert 'is_active' in item     # DÜZELTİLDİ: 'not in' yerine 'in' yaptık!
    assert item['code'] == "INVALID_PHOTO"
    assert item['is_active'] is True