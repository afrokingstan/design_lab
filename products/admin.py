from django.contrib import admin
from .models import Extra, Product, Category, Design_Packs

# Register your models here.


class ExtraAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'category',
        'image',
    )
    ordering = ('sku',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'image',
    )
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


class Design_packsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'description',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Extra, ExtraAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Design_Packs, Design_packsAdmin)
