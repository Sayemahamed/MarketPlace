from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ItemForm

# Create your views here.
@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('core:index')
    return render(request, 'item/create_item.html', {
        'form': ItemForm(), 
        'title': 'Create Item'
        })