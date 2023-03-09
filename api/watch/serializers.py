from rest_framework import serializers
from .models import Watch, Color, Brand, Category, Size
from rest_framework.validators import UniqueValidator


class ColorSerializer(serializers.ModelSerializer):
    color_name = serializers.CharField(
        max_length=50, validators=[UniqueValidator(queryset=Color.objects.all())]
    )

    class Meta:
        model = Color
        fields = "__all__"


class SizeSerializer(serializers.ModelSerializer):
    size_name = serializers.CharField(
        max_length=50, validators=[UniqueValidator(queryset=Size.objects.all())]
    )

    class Meta:
        model = Size
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(
        max_length=50, validators=[UniqueValidator(queryset=Brand.objects.all())]
    )

    class Meta:
        model = Brand
        exclude = ("brand_slug",)


class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        max_length=50, validators=[UniqueValidator(queryset=Category.objects.all())]
    )

    class Meta:
        model = Category
        exclude = ("category_slug",)


class WatchSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    color = ColorSerializer()
    color_available = ColorSerializer(many=True)
    size = SizeSerializer()
    size_available = SizeSerializer(many=True)
    watch_name = serializers.CharField(
        max_length=50, validators=[UniqueValidator(queryset=Watch.objects.all())]
    )

    class Meta:
        model = Watch
        exclude = ("watch_slug",)
