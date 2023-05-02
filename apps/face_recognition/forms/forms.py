from django import forms

from apps.face_recognition.models import FaceRecognition


class FaceRecognitionForm(forms.ModelForm):
    class Meta:
        model = FaceRecognition
        fields = '__all__'
