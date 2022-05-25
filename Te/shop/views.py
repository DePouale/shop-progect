from django.views.generic import ListView, DetailView
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import *
from .utils import *

menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Новости", 'url_name': 'news'},
        {'title': "О нас", 'url_name': 'about'},
        {'title': "Чайный магазинчик", 'url_name': 'category'},
        {'title': "Корзина", 'url_name': 'cart'}
        ]

# Главная Страница .
class ShopHome(DataMixin, ListView):
    model = ProductPhoto
    template_name = 'shop/index.html'
    context_object_name = 'product' 

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

# Главная Страница - механизм показа категорий.
class ShopCategory(DataMixin, ListView):
    model = ProductPhoto
    template_name = 'shop/index.html'
    context_object_name = 'product'
    allow_empty = False
    
    def get_queryset(self):
        return ProductPhoto.objects.filter(product__category__slug=self.kwargs['categories_slug'])
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Катеория - ' + str(context['product'][0].product.category),
                                              cat_selected=context['product'][0].product.category_id)
        return dict(list(context.items()) + list(c_def.items()))
    
#Страница продукта(товара)   
class ShowProduct(DataMixin, DetailView):
    model = ProductPhoto
    template_name = "shop/product.html"
    slug_field = 'product__slug'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['product'])
        return dict(list(context.items()) + list(c_def.items()))
    

# Create your views here.
""" def index(request):
    #product = Product.objects.all()
    product = ProductPhoto.objects.all()
    context = {
        'product': product,
        'menu': menu, 
        'title': 'Главная',
        'cat_selected': 0,
        }
    
    return render(request, "shop/index.html", context=context) """

def category(request):
    сategory = Category.objects.all()
    context = { 
        'сategory': сategory,       
        'menu': menu, 
        'title': 'Чайный магазинчик'
        }
    return render(request, "shop/category.html", context=context)

#Разбивка по Slug Категории
""" def show_categories(request, categories_slug):
    product = ProductPhoto.objects.filter(product__category__slug=categories_slug)
    context = {
        'product': product, 
        'menu': menu, 
        'title': '',
        'cat_selected': categories_slug,
        }
    
    return render(request, "shop/index.html", context=context) """

def about(request):
    context = {
        'menu': menu, 
        'title': 'О нас'
        }
    return render(request, "shop/about.html", context=context)
def news(request):
    context = { 
        'menu': menu, 
        'title': 'Новости'
        }
    return render(request, "shop/news.html", context=context)
#Страница продукта
""" def product(request, product_slug):
    product = get_object_or_404(ProductPhoto, product__slug=product_slug)
    
    context = {
        'product': product,
        'menu': menu, 
        'title': 'Новости',
        'cat_selected': product.product.category_id,
    }
    return render(request, "shop/product.html", context=context) """



    
def cart(request):
    context = { 
        'menu': menu, 
        'title': 'Корзина'
        }
    return render(request, "shop/cart.html", context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')