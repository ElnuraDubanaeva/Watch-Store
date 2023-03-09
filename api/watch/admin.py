from django.contrib import admin
from .models import Watch, Color, Category, Brand, Size


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"category_slug": ("category_name",)}


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"brand_slug": ("brand_name",)}


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ["watch_name", "category", "year", "color", "brand"]
    list_display_links = ("watch_name",)
    prepopulated_fields = {"watch_slug": ("watch_name",)}
    ordering = ("watch_name", "year", "brand", "id", "price", "size")
    list_per_page = 10
    list_filter = ("watch_name", "color", "price", "brand", "year")
    search_fields = ("watch_name", "description", "vrand")


admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
