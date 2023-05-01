from django.urls import path
from api.face_recognition.views.views import FaceRecognitionTemplateView

urlpatterns = [
    path('', FaceRecognitionTemplateView.as_view(), name='face_recognition'),
]
