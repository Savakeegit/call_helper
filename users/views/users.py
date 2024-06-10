import pdb

from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers.api import users as user_serializers

User = get_user_model()


@extend_schema_view(
    post=extend_schema(summary='Регистрация пользователя', tags=['Аутентификация & Авторизация']),
)
class RegistrationView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = user_serializers.RegistrationSerializer


@extend_schema_view(
    post=extend_schema(
        request=user_serializers.ChangePasswordSerializer,
        summary='Смена пароля',
        tags=['Аутентификация & Авторизация'],
    ),
)
class ChangePasswordView(APIView):

    def post(self, request):
        serializer = user_serializers.ChangePasswordSerializer(
            instance=request.user,
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


@extend_schema_view(
    get=extend_schema(summary='Профиль пользователя', tags=['Пользователи'],),
    put=extend_schema(summary='Изменить профиль пользователя', tags=['Пользователи'],),
    patch=extend_schema(summary='Частично изменить профиль пользователя', tags=['Пользователи'],),
)
class MeView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializers.MeSerializer
    http_method_names = ('get', 'patch',)

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return user_serializers.MeUpdateSerializer
        return user_serializers.MeSerializer

    def get_object(self):
        return self.request.user