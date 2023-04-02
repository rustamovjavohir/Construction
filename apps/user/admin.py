from django.contrib import admin

from apps.user.models import User


# Register your models here.


@admin.register(User)
class B2CCommandTextAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "phone", "message", "email", "is_done", "created_at"]
    list_display_links = ["id", "username"]
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = (
        ('Основной', {'fields': ('username', 'auth_type', 'phone', 'email')}),
        ('Дополнительно', {'fields': ('message', 'status', 'is_done')}),
        ('Системные', {'fields': ('password', 'full_name', 'created_at', 'updated_at')})
    )
