from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.exceptions import NotAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import TemplateView

from api.auth_user.serializers.serializers import CustomObtainPairSerializer, CustomTokenRefreshSerializer, \
    LogoutSerializer, CustomUserProfilesSerializer


# Create your views here.
class LoginView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer

    def post(self, request, *args, **kwargs):
        print('LoginView')
        return super().post(request, *args, **kwargs)


class GetRefreshTokenView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        return super(GetRefreshTokenView, self).post(request, *args, **kwargs)


class LogoutView(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            refresh_token = serializer.validated_data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            data = {
                'success': True,
                "message": "You are logged out"
            }
            return Response(data=data, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            data = {"error": str(e)}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class CustomUserView(GenericAPIView):
    serializer_class = CustomUserProfilesSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        if isinstance(exc, NotAuthenticated):
            response.data['success'] = False
            response.data['statusCode'] = exc.status_code
            response.data['code'] = exc.default_code
            response.data['message'] = exc.detail
            response.data['result'] = None
            response.status_code = status.HTTP_200_OK
            response.data.pop('detail')
        return response

    @extend_schema(summary="Foydalanuvchi haqidagi malumotlarini chop etish (retrieve)")
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return JsonResponse(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


class CustomTemplateView(TemplateView):
    template_name = 'authorization/login.html'

    def get(self, request, *args, **kwargs):
        context = {}
        if request.user.is_authenticated:
            return redirect('admin:index')
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('admin:index')
        else:
            context = {}
            return render(request, self.template_name, context=context)
