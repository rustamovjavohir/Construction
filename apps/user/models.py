from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.

class User(models.Model):
    class Status(models.TextChoices):
        # Field = (for database, for UI)
        ACTIVE = ("active", "Active")
        INACTIVE = ("inactive", "Inactive")
        DELETED = ("deleted", "Deleted")

    class AuthTypeChoices(models.TextChoices):
        # Field = (for database, for UI)
        VIA_USERNAME = ("via_username", "Via Username")
        VIA_EMAIL = ("via_email", "Via Email")
        VIA_PHONE = ("via_phone", "Via Phone")
        VIA_TELEGRAM = ("via_telegram", "Via Telegram")

    username = models.CharField(max_length=250, verbose_name="Логин", unique=True)
    password = models.CharField(max_length=250, verbose_name="Пароль")
    full_name = models.CharField(max_length=250, verbose_name="Имя Фамилия", null=True, blank=True)
    phone = models.CharField(max_length=15, verbose_name="Телефон", null=True, blank=True)
    message = models.TextField(blank=True, null=True, verbose_name="Сообщение")
    email = models.CharField(max_length=250, null=True, blank=True, verbose_name="Email")
    is_done = models.BooleanField(default=False, verbose_name="Выполнено")
    auth_type = models.CharField(max_length=250, choices=AuthTypeChoices.choices,
                                 default=AuthTypeChoices.VIA_USERNAME, verbose_name="Тип авторизации")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True, blank=True)
    is_deleted = models.BooleanField(default=False, verbose_name="Удален")
    status = models.CharField(max_length=250, choices=Status.choices, default=Status.INACTIVE, verbose_name="Статус")

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.status == User.Status.DELETED:
            self.is_deleted = True
        self.set_password(self.password)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["-id"]
