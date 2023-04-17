from uuid import uuid4

from django.db import models
from django.utils.text import slugify


# Create your models here.


class Advertising(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='Advertising', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    finished_at = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True, db_index=True, verbose_name="URL")

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-id']
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"

    def __str__(self):
        return self.title
