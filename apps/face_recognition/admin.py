from django.contrib import admin
from django.utils.html import format_html
from django.utils.text import capfirst

from apps.face_recognition.forms import FaceRecognitionForm
from apps.face_recognition.models import FaceRecognition


# Register your models here.


@admin.register(FaceRecognition)
class FaceRecognitionAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'age', 'view_age', 'image', 'full_information', 'is_deleted')
    empty_value_display = '-empty-'
    date_hierarchy = 'created_at'
    filter_horizontal = ('user_many',)
    # fields = [('user', 'name'), 'age', 'image']
    readonly_fields = ('full_information',)
    # raw_id_fields = ('user',)
    autocomplete_fields = ('user',)
    # radio_fields = {"user": admin.VERTICAL}
    # show_full_result_count = False
    search_fields = ('name',)
    search_help_text = "Поиск по имени"  # jazzminda ishlamaydi

    fieldsets = (
        ("Personal", {
            'fields': ['user', 'name', 'age', 'user_many', 'full_information'],
            'classes': ('wide', 'extrapretty')
        }),
        ("Image", {
            'fields': ('image',)
        })
    )

    @admin.display(empty_value="???", description="Age2")
    def view_age(self, obj):
        return obj.age

    @admin.display
    def full_information(self, obj):
        return format_html(
            '<a href="{}/change/">{}</a>', obj.id, obj.name
        )

    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])
            for model in app['models']:
                model['name'] = capfirst(model['name'])
        return app_list


FaceRecognitionAdmin.actions_on_top = True
FaceRecognitionAdmin.actions_selection_counter = True


# @admin.register(FaceRecognition)
class FaceFormAdmin(admin.ModelAdmin):
    form = FaceRecognitionForm
