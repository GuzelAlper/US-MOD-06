from rest_framework import generics
from .models import BlockingReason
from .serializers import BlockingReasonSerializer

class ActiveBlockingReasonsList(generics.ListAPIView):
    serializer_class = BlockingReasonSerializer

    def get_queryset(self):
        # Sadece aktif olan (is_active=True) nedenleri döndürür
        return BlockingReason.objects.filter(is_active=True)