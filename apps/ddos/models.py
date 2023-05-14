from django.db import models


# Create your models here.
class BlackIps(models.Model):
    INTERVAL_TIME = 18000  # soat

    ip = models.CharField(max_length=15, unique=True)
    reason = models.CharField(max_length=50, default='unknown')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def check_is_active(self):
        if self.is_active:
            if (self.updated_at - self.created_at).seconds > self.INTERVAL_TIME:
                self.is_active = True
                self.save()
            return self.is_active
