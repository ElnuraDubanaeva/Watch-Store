from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import WatchViewSet, ColorViewSet, BrandViewSet, CategoryViewSet, SizeViewSet

router = SimpleRouter()
router.register("watch", WatchViewSet, basename="watch")
router.register("brand", BrandViewSet, basename="brand")
router.register("color", ColorViewSet, basename="color")
router.register("size", SizeViewSet, basename="size")
router.register("category", CategoryViewSet, basename="category")
urlpatterns = [path("", include(router.urls))]
