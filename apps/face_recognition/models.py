from django.db import models
from apps.auth_user.models import CustomUser


# Create your models here.


class FaceRecognition(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='face_recognition/')
    age = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    user_many = models.ManyToManyField(CustomUser, related_name='user_many')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Face Recognition'
        verbose_name_plural = 'Face Recognition'
        permissions = (
            ('view_index', 'Can view index'),
        )
