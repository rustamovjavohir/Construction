from django.template.response import TemplateResponse
from django.urls import path, reverse

from django.contrib import admin
from django.utils.html import format_html

from apps.apartment.models import Apartment, Floor


# Register your models here.

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "room_quantity", "area", "floor", "price", "image_3d", "image_2d", "image"]


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ["id", "floor_id", "name", "report"]
    request = None

    def get_queryset(self, request):
        qs = super(FloorAdmin, self).get_queryset(request)
        self.request = request
        return qs

    def report(self, obj):
        args = [obj.id, ]
        url = self.request.build_absolute_uri(reverse('detail', args=args))
        return format_html(f'<a href={url}>Detail</a>')

    report.short_description = "Info"


class ImportCSVData(Floor):
    class Meta:
        proxy = True


@admin.register(ImportCSVData)
class MyModelAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('my_view/', self.my_view),
        ]
        return my_urls + urls

    def my_view(self, request):
        context = dict(
            # Include common variables for rendering the admin template.
            self.admin_site.each_context(request),
            # Anything else you want in the context...
            key="salom",
            # key=value,
        )
        return TemplateResponse(request, "sometemplate.html", context)

# class MyAdmin(admin.ModelAdmin):
#     def get_urls(self):
#         urls = super().get_urls()
#         my_urls = [
#             path('my-view/', self.admin_site.admin_view(CustomAdminView.as_view)),
#         ]
#         return my_urls + urls
#
#
# admin.site.register(Floor, MyAdmin)


# class CustomAdminSite(admin.AdminSite):  # 1.
#     site_header = "Custom Admin Site header"
#     site_title = "Custom Admin Site title"
#
#     def get_urls(self):  # 2.
#         urls = super().get_urls()
#         my_urls = [
#             path('custom_admin_view/',
#                  self.admin_view((  # 3.
#                      CustomAdminView.as_view(admin_site=self))), name='cav'),
#         ]
#         return my_urls + urls  # 4.
#
#
# admin_site = CustomAdminSite(name='myadmin')  # 5.
# admin_site.register(Floor)
