from django.contrib import admin
from . import models

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(models.Category, CategoriesAdmin)
admin.site.register(models.Products, ProductsAdmin)

