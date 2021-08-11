from django.shortcuts import render
from basketapp.models import Basket
from mainapp.context_processors import basket
from mainapp.models import Product


def index(request):
    title = 'магазин'

    products = Product.objects.filter(is_deleted=False, category__is_deleted=False)[:3]

    context = {
        'title': title,
        'products': products,
        'basket': basket
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'контакты'
    context = {
        'title': title
    }
    return render(request, 'geekshop/contact.html', context=context)
