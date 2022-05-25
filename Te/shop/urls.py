from django.urls import path
from .views import ShopHome, about, news, category, ShowProduct, cart, ShopCategory

urlpatterns = [
    path('', ShopHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('news/', news, name='news'),
    path('category/', category, name='category'),
    path('product/<slug:product_slug>/', ShowProduct.as_view(), name='product'),
    path('cart/', cart, name='cart'),
    path('categories/<slug:categories_slug>', ShopCategory.as_view(), name='categories'),
]

