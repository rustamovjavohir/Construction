from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.auth_user.models import CustomUser
from apps.face_recognition.models import FaceRecognition


# Register your models here.
class FaceRecognitionInline(admin.StackedInline):
    model = FaceRecognition
    extra = 1
    fields = ('user', 'name', 'age', 'image')


@admin.register(CustomUser)
class AdminUser(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_per_page = 25
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    readonly_fields = ('last_login',)
    UserAdmin.fieldsets += (
        ('Профиль', {'fields': ('photo', 'telegram_id')}),
    )

    inlines = [FaceRecognitionInline]
