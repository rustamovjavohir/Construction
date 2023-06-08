from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from rest_framework.views import APIView
from django.views.generic import TemplateView, ListView
from django.contrib.admin import site


# Create your views here.


class FaceRecognitionTemplateView(TemplateView):
    template_name = 'face_recognition/face_recognition.html'

    # template_name = 'face_recognition/image_input.html'

    def post(self, request):
        apps = site.get_app_list(request)
        print(request.POST)
        print(request.FILES['picture'])
        image = request.FILES['picture']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        context = {
            'uploaded_file_url': uploaded_file_url,
            'apps': apps,
        }
        return render(request, self.template_name, context=context)

    def get(self, request):
        apps = site.get_app_list(request)
        context = {
            'apps': apps,
        }
        return render(request, self.template_name, context=context)


class FaceRecognitionAPIView(APIView):
    pass


class Preferences(ListView):
    admin = {}

    def get(self, request):
        ctx = self.admin.each_context(request)
        return render(request, 'face_recognition/index.html', ctx)


def my_custom_view(request):
    return render(request, 'face_recognition/index.html')
