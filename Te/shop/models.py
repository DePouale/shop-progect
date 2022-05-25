from tabnanny import verbose
from django.db import models
from django.urls import clear_script_prefix, reverse

# Create your models here.
class Product(models.Model):
    name_product = models.CharField(max_length=150,  verbose_name="Название товара")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    description_product = models.TextField(verbose_name="Описание товара")
    image = models.ImageField(upload_to="photos_product/%Y/%m/%d/", verbose_name="Фото", null=True)
    price_product = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")
    
    def __str__(self):
        return self.name_product
    
    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['time_create', 'name_product']
        
class ProductPhoto(models.Model):

    product = models.ForeignKey('Product', on_delete=models.DO_NOTHING, related_name='images')
    image = models.ImageField(upload_to='products_product/%Y/%m/%d', blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.product.name_product
              
class Category(models.Model):

    name = models.CharField(max_length=50, db_index=True, verbose_name="Вид чая")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField()
    photo = models.ImageField(upload_to="photos_category/%Y/%m/%d/", verbose_name="Фото")
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('categories', kwargs={'categories_slug': self.slug})
    
    class Meta:
        verbose_name = "Вид чая или посуды"
        verbose_name_plural = "Виды чая, посуда"
        ordering = ['id']
    
