from django.urls import path
from api.face_recognition.views.views import FaceRecognitionTemplateView, my_custom_view

urlpatterns = [
    path('', FaceRecognitionTemplateView.as_view(), name='face_recognition'),
    path('index/', my_custom_view, name='face_recognition_index'),
]
