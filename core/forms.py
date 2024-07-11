from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
        username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
        password=forms.CharField( widget=forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class':'w-full py-4 px-6 rounded-xl'
    }))

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )