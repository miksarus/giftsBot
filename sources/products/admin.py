from django.contrib import admin

from .forms import ProductForm
from .models import Category, Product, Mark


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')
    

@admin.register(Product)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ozone_id', 'category', 'update_date')
    form = ProductForm

@admin.register(Mark)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
