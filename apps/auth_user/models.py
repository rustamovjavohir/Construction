from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    telegram_id = models.BigIntegerField(verbose_name="Телеграм ID", null=True, blank=True)
    photo = models.ImageField(upload_to='user_photo', verbose_name="Фото", null=True, blank=True)
