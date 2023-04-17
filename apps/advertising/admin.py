from django.contrib import admin
from apps.advertising.models import Advertising


# Register your models here.

@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'description', 'created_at', 'finished_at', 'is_deleted', 'slug')
    list_display_links = ('id', 'title', 'slug')
    search_fields = ('id', 'title', 'image', 'description', 'created_at', 'finished_at', 'is_deleted', 'slug')
    list_filter = ('finished_at', 'is_deleted')
    # prepopulated_fields = {'slug': ('title',)}
