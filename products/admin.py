from django.contrib import admin
from .models import Product, Category, Brand, ProductTag


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'brand',
        'image',
    )
    search_fields = ['sku', 'name', 'brand']
    ordering = ('sku',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    ordering = ('friendly_name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'website',
    )
    ordering = ('name',)


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'search_visible',
    )
    ordering = ('name',)
