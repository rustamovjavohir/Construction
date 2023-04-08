from django.http import JsonResponse
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.auth_user.serializers.serializers import CustomObtainPairSerializer, CustomTokenRefreshSerializer, \
    LogoutSerializer, CustomUserProfilesSerializer


# Create your views here.
class LoginView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer


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

    @extend_schema(summary="Foydalanuvchi haqidagi malumotlarini chop etish (retrieve)")
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return JsonResponse(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
