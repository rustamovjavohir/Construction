from django.contrib import admin
from apps.face_recognition.models import FaceRecognition


# Register your models here.
@admin.register(FaceRecognition)
class FaceRecognitionAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'image')
