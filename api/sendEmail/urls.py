from django.urls import path
from api.sendEmail.views.views import *

urlpatterns = [
    path('send/', SendEmail.as_view(), name='send-email'),
    path('list/', EmailListView.as_view(), name='email-list'),
    path('delete/<int:pk>/', EmailDestroyAPIView.as_view(), name='email-delete'),
    path('<int:pk>/', EmailDetail.as_view(), name='email-retrieve')
]
