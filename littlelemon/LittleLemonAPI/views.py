from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem
from .serializer import MenuItemSerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.

class SingleMenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser]
    
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser]