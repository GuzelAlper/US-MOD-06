from rest_framework import serializers
from .models import BlockingReason

class BlockingReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockingReason
        fields = ['id', 'title', 'hard_block']