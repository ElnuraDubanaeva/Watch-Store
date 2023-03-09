from django.db import models
from pytils import translit
from .utils import path_and_rename


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(
        max_length=50, unique=True, db_index=True, verbose_name="Категория"
    )
    category_slug = models.SlugField(unique=True, db_index=True, default="")

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        self.category_slug = translit.slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категорий"
        ordering = ("category_name",)


class Brand(models.Model):
    brand_name = models.CharField(
        max_length=50, unique=True, db_index=True, verbose_name="Бренд"
    )
    brand_slug = models.SlugField(unique=True, db_index=True, default="")

    def __str__(self):
        return self.brand_name

    def save(self, *args, **kwargs):
        self.brand_slug = translit.slugify(self.brand_name)
        super(Brand, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"
        ordering = ("brand_name",)


class Color(models.Model):
    color_name = models.CharField(
        max_length=50, unique=True, db_index=True, verbose_name="Цвет"
    )

    def __str__(self):
        return self.color_name

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"
        ordering = ("color_name",)


class Size(models.Model):
    size_name = models.CharField(
        max_length=50, unique=True, db_index=True, verbose_name="Размер"
    )

    def __str__(self):
        return self.size_name

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"
        ordering = ("size_name",)


class Watch(models.Model):
    watch_name = models.CharField(
        max_length=50, unique=True, db_index=True, verbose_name="Название"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="category",
        verbose_name="Категория",
    )
    year = models.DateField(blank=True, null=True, verbose_name="Год выпуска")
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE, related_name="color", verbose_name="Цвет"
    )
    price = models.PositiveSmallIntegerField(verbose_name="Цена")
    discount = models.PositiveSmallIntegerField(
        default=0, blank=True, null=True, verbose_name="Скидка"
    )
    watch_slug = models.SlugField(unique=True, db_index=True, default="")
    amount = models.IntegerField(verbose_name="Количество в наличий")
    is_available = models.BooleanField(default=True, verbose_name="В наличии")
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name="brand",
        verbose_name="Бренд",
    )
    color_available = models.ManyToManyField(
        Color, related_name="color_available", verbose_name="Цвета в наличии"
    )
    size = models.ForeignKey(
        Size, on_delete=models.CASCADE, related_name="size", verbose_name="Размер"
    )
    size_available = models.ManyToManyField(
        Size, related_name="size_available", verbose_name="Размеры в наличий"
    )
    image = models.ImageField(
        upload_to=path_and_rename,
        null=True,
        blank=True,
        default="",
        verbose_name="Изображения",
    )
    posted_date = models.DateField(auto_now_add=True, verbose_name="Дата опубликования")
    updated_date = models.DateField(auto_now=True, verbose_name="Дата обновления")
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.watch_name

    def save(self, *args, **kwargs):
        self.watch_slug = translit.slugify(self.watch_name)
        super(Watch, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Часы"
        verbose_name_plural = "Часы"
        ordering = ("watch_name", "brand", "price")
