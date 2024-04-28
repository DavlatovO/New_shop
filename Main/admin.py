from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'get_image', )

    def get_image(self, product):
        if product.image:
            return mark_safe(f"<img src='{product.image.url}' width='75px' style='border-radius:15px' />")


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)





admin.site.register(models.Category, CategoriesAdmin)
admin.site.register(models.Products, ProductsAdmin)

