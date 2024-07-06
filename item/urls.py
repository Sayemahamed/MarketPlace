from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('<int:item_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('<int:item_id>/delete/', views.delete, name='delete'),
    path('<int:item_id>/edit/', views.edit, name='edit'),
    path('search/', views.search, name='search'),
]