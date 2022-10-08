from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    is_telegram = models.BooleanField(default=False)
    is_web = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
