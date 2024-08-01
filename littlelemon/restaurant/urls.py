from django.contrib import admin 
from django.urls import path 
from .views import MenuItemsView, SingleMenuItemView, index


  
urlpatterns = [ 
    path('', index, name='index'), 
    path('menu/',MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]