from django.contrib import admin

from apps.user.models import User


# Register your models here.


@admin.register(User)
class B2CCommandTextAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone", "message", "email",
                    "is_telegram", "is_web", "is_done", "created_at"]
