from django.contrib import admin

# Register your models here.
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'slug', 'stock', 'image','available']
    list_editable = ['price', 'stock', 'image','available']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Product,ProductAdmin)
