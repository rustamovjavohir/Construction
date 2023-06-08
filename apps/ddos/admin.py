from django.contrib import admin
from apps.ddos.models import BlackIps


# Register your models here.

@admin.register(BlackIps)
class BlackIpsAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'reason', 'is_active', 'created_at')
    list_display_links = ('id', 'ip')
    search_fields = ('ip', 'reason')
    list_per_page = 25
