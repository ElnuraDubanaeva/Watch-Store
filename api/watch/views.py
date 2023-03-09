from rest_framework.viewsets import ModelViewSet
from .models import Watch, Color, Category, Brand, Size
from .serializers import (
    ColorSerializer,
    BrandSerializer,
    CategorySerializer,
    WatchSerializer,
    SizeSerializer
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class WatchViewSet(ModelViewSet):
    queryset = Watch.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = "watch_slug"
    serializer_class = WatchSerializer
    authentication_classes = (JWTAuthentication,)
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ("watch_name",)
    ordering_fields = ("price", "year")


class ColorViewSet(ModelViewSet):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()
    permission_classes = (IsAdminUser,)
    lookup_field = "id"


class SizeViewSet(ModelViewSet):
    serializer_class = SizeSerializer
    queryset = Size.objects.all()
    permission_classes = (IsAdminUser,)
    lookup_field = "id"


class BrandViewSet(ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = (IsAdminUser,)
    lookup_field = "brand_slug"


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAdminUser,)
    lookup_field = "category_slug"
