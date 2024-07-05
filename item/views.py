from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from .models import Item
from .forms import NewProductForm


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item_id)
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })
@login_required
def new(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', item.id)
    form = NewProductForm()
    return render(request, 'item/form.html', {
        'form': form ,
        'title': 'New Product'
    })