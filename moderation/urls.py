from django.urls import path
from .views import ActiveBlockingReasonsList

urlpatterns = [
    path('product-blocking-reasons/', ActiveBlockingReasonsList.as_view(), name='product-blocking-reasons'),
]