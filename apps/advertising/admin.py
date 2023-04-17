from django.contrib import admin
from apps.advertising.models import Advertising


# Register your models here.

@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'created_at', 'finished_at', 'is_deleted', 'slug')
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'image', 'description', 'created_at', 'finished_at', 'is_deleted', 'slug')
    list_filter = ('finished_at', 'is_deleted')
    # prepopulated_fields = {'slug': ('title',)}
