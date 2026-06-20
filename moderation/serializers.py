from rest_framework import serializers
from .models import BlockingReason

class BlockingReasonSerializer(serializers.ModelSerializer):
    # UUID'nin dışarıya düzgün bir string formatında verilmesini garanti ediyoruz
    id = serializers.UUIDField(format='hex_verbose', read_only=True)

    class Meta:
        model = BlockingReason
        # Hakemin istediği tüm alanları ekledik:
        fields = ['id', 'code', 'title', 'hard_block', 'is_active']