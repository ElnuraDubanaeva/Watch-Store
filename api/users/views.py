from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAdminUser


# Create your views here.
class RegisterViewSet(ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    http_method_names = ("post",)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return Response(
            status=status.HTTP_201_CREATED, data={"success": "user created"}
        )


class LoginViewSet(ModelViewSet):
    serializer_class = LoginSerializer
    queryset = User.objects.all()
    http_method_names = ("post", "update")
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get("username")
        user = authenticate(**serializer.validated_data)
        if user:
            user = User.objects.get(username=username)
            refresh = RefreshToken.for_user(user)
            return Response(
                status=status.HTTP_200_OK,
                data={"access": str(refresh.access_token), "refresh": str(refresh)},
            )
        return Response(
            status=status.HTTP_403_FORBIDDEN, data={"error": "Invalid credentials"}
        )


class UsersViewSet(ModelViewSet):
    serializer_class = RegisterSerializer
    http_method_names = ("get", "list", "retrieve")
    lookup_field = "id"
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
