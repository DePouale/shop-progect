from django.contrib import admin
from .models import Product, Category,ProductPhoto
# Register your models here.



class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    fk_name = "product"
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product', 'time_create','is_published')
    list_display_links = ('id', 'name_product')
    search_fields = ('name_product', 'description_product')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    inlines = [
        ProductPhotoInline,
    ]
    prepopulated_fields = {"slug": ('name_product',)}
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    prepopulated_fields = {"slug": ('name',)}


    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductPhoto)