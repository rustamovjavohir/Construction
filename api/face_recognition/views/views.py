from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from rest_framework.views import APIView
from django.views.generic import TemplateView


# Create your views here.


class FaceRecognitionTemplateView(TemplateView):
    template_name = 'face_recognition/face_recognition.html'
    # template_name = 'face_recognition/image_input.html'

    def post(self, request):
        print(request.POST)
        print(request.FILES['picture'])
        image = request.FILES['picture']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        context = {
            'uploaded_file_url': uploaded_file_url
        }
        return render(request, self.template_name, context=context)

    def get(self, request):
        print("salom")
        return render(request, self.template_name, context={})


class FaceRecognitionAPIView(APIView):
    pass
