from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','price','image',)
        widgets = {
            'category': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl border'}),
            'name': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl border'}),
            'price': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl border'}),
            'image': forms.FileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl border'}),
        }