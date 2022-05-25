from .models import *
from django.db.models import Count

menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Новости", 'url_name': 'news'},
        {'title': "О нас", 'url_name': 'about'},
        {'title': "Чайный магазинчик", 'url_name': 'category'},
        {'title': "Корзина", 'url_name': 'cart'}
        ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('product'))
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context