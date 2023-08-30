from django.urls import path
from api.billing.views import PaymeCallBackAPIView

urlpatterns = [
    path("payments/merchant/", PaymeCallBackAPIView.as_view()),
]
