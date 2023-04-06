from django.db import transaction
from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework import filters, status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.user.models import User
from api.user.serializers.serializers import UserSerializer, CustomObtainPairSerializer, CustomTokenRefreshSerializer, \
    LogoutSerializer, CustomUserProfilesSerializer


# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    parser_classes = [JSONParser, ]

    # permission_classes = [IsAdminUser, ]
    # authentication_classes = [JWTAuthentication, ]

    @extend_schema(summary='Foydalanuvchilar royhatini chop etish')
    def list(self, request, *args, **kwargs):
        return super(UserViewSet, self).list(self, request, *args, **kwargs)

    @transaction.atomic
    @extend_schema(summary="Foydalanuvchi kirish")
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @transaction.atomic
    @extend_schema(summary="Foydalanuvchi malumotlarini yangilash")
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @transaction.atomic
    @extend_schema(summary="Foydalanuvchi malumotlarini qisman yangilash")
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @extend_schema(summary="Foydalanuvchi malumotlarini o'chirish")
    def destroy(self, request, *args, **kwargs):
        return super(UserViewSet, self).destroy(self, request, *args, **kwargs)

    @extend_schema(summary="Foydalanuvchi haqidagi malumotlarini chop etish (retrieve)")
    def retrieve(self, request, *args, **kwargs):
        return super(UserViewSet, self).retrieve(self, request, *args, **kwargs)


# test branch

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
        return JsonResponse(serializer.data)
