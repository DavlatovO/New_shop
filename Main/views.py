from django.shortcuts import render, get_object_or_404
from . import models

def index(request,):
   products = models.Products.objects.all()
   category = models.Category.objects.all()

   context = {
      'products':products,
      'category':category
   }
   return render(request, 'index.html', context)

def shop(request):

   return render(request, 'shop.html')
