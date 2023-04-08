from django.db import models

from apps.apartment.models import Apartment
from apps.user.models import User


# Create your models here.

class Order(models.Model):
    class Status(models.TextChoices):
        # Field = (for database, for UI)
        PENDING = ('PENDING', 'Pending')
        IN_PROGRESS = ('IN_PROGRESS', 'In Progress')
        CANCELLED = ('CANCELED', 'Cancelled')
        COMPLETED = ('COMPLETED', 'Completed')

    name = models.CharField(max_length=250, verbose_name="Наименование товара", default="Order")
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, verbose_name="Квартира")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    status = models.CharField(max_length=250, choices=Status.choices, default=Status.PENDING, verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_deleted = models.BooleanField(default=False, verbose_name="Удален")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-created_at']

    def __str__(self):
        return self.name
