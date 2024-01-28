from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_filter = ('category',)


@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'description', 'price', 'delivery_fee')
    list_display_links = ('image_preview', 'description')
    list_filter = ('subcategory__name',)
    search_fields = ('description', 'price',
                     'delivery_fee', 'subcategory__name')

    def image_preview(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))

    image_preview.short_description = 'Preview'
