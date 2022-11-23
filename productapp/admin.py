from django.contrib import admin

from .models import CategoryList, ProductList


@admin.register(CategoryList)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


@admin.register(ProductList)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'is_active')
    list_display_links = ('id', 'title', 'category', 'price', 'is_active')
    search_fields = ('title', 'category')
