from django import forms
from .models import ConversationMessage
from item.models import Item
from django.contrib.auth.models import User

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl border'})

        }