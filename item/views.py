from django.shortcuts import render, get_object_or_404
from .models import Item


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item/detail.html', {
        'item': item
    })