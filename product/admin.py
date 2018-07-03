from django.contrib import admin
from .models import Product, After
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','user','title','content','update_at']
    list_display_links = ['title']


@admin.register(After)
class AfterAdmin(admin.ModelAdmin):
    list_display = ['id','author','message','update_at']
    list_display_links = ['message']
