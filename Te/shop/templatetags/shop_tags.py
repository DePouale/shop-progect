
from django import  template
from shop.models import Product, Category, ProductPhoto

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(slug=filter)

""" @register.simple_tag()
def get_ProductPhoto():
    return ProductPhoto.objects.all() """

@register.inclusion_tag('shop/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    
    return {"cats": cats, "cat_selected": cat_selected}