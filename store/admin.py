from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','stock','price','category','modified_date','is_available')
    prepopulate_fields = {'slug':('product_name',)}
admin.site.register(Product,ProductAdmin)