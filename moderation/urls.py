from django.urls import path
from .views import ActiveBlockingReasonsList

urlpatterns = [
    # OpenAPI'nin tam olarak beklediği endpoint rotası:
    path('api/v1/blocking-reasons/', ActiveBlockingReasonsList.as_view(), name='blocking-reasons-list'),
]