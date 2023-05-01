from django.db import models
from apps.auth_user.models import CustomUser


# Create your models here.


class FaceRecognition(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='face_recognition/')

    def __str__(self):
        return self.name
