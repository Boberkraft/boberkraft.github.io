from django.contrib import admin
from django import forms
from django.conf import settings
# Register your models here.
from .models import Product
from .forms import ProductForm

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']

    form = ProductForm



admin.site.register(Product, ProductAdmin)