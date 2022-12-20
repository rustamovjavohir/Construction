from django.db import models


# Create your models here.


class Email(models.Model):
    subject = models.CharField(null=True, blank=True, max_length=250)
    message = models.TextField()
    email = models.EmailField(max_length=250)
    recipient = models.EmailField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["-id"]
