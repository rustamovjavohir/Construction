from django.db import models


# Create your models here.


class Advertising(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='Advertising', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    finished_at = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"

    def __str__(self):
        return self.title
