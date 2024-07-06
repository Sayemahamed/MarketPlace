from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from .models import Item
from .forms import NewProductForm, EditProductForm


def search(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(is_sold=False)
    if query:
        items = items.filter(name__icontains=query,is_sold=False)
    return render(request, 'item/search.html',{
        'items': items,
        'query': query
    })
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

@login_required
def delete(request, item_id):
    item = get_object_or_404(Item, pk=item_id, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

@login_required
def edit(request, item_id):
    item = get_object_or_404(Item, pk=item_id, created_by=request.user)
    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('item:detail', item.id)
    else:
        form = EditProductForm(instance=item)
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit Product'
    })
