from django.contrib import admin
from .models import Product
# Register your models here.

# class ProductAdmin(admin.ModelAdmin):
#     fields = ['name ', 'description ']
#     list_display = ('name ', 'description ')
#     search_fields = ['name ', 'description ']

admin.site.register(Product)
