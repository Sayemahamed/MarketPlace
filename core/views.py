from django.shortcuts import render
from item.models import Item, Category
# Create your views here.

def index(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'items': items,
        'categories': categories
        })