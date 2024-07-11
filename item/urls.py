from django.urls import path
from . import views

app_name = 'item'
urlpatterns = [
    path('create_item/', views.create_item, name='create_item'),
]