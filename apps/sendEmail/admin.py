from django.contrib import admin
from apps.sendEmail.models import Email


# Register your models here.

@admin.register(Email)
class AdminEmail(admin.ModelAdmin):
    list_display = ["id", "subject", "message", "email", 'phone', "recipient", "is_deleted", "created_at"]
