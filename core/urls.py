from django.contrib.auth.views import LoginView
from django.urls import path
from .forms import LoginForm
from . import views

app_name = 'core'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login'),
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='index'),
]