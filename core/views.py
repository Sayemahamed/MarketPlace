from django.shortcuts import render
from item.models import Item, Category
from .forms import SignUpForm
# Create your views here.

def index(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'items': items,
        'categories': categories
        })
def signup(request):
    return render(request, 'core/signup.html')