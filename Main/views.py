from django.shortcuts import render, get_object_or_404
from . import models

def index(request):
   products = models.Products.objects.all()
   category = models.Category.objects.all()

   context = {
      'products':products,
      'category':category
   }
   return render(request, 'index.html', context)

def shop(request):
   products = models.Products.objects.all()
   category = models.Category.objects.all()
   context = {
      'products':products,
      'category':category
      
   }      
   return render(request, 'shop.html', context)

from django.shortcuts import render, get_object_or_404

def shop_detail(request, slug):
    categories = models.Category.objects.all()
    product = get_object_or_404(models.Products, slug=slug)
    reviews = models.Review.objects.filter(product=product)
    
   
    total_marks = sum(review.mark for review in reviews)
    num_reviews = reviews.count()
    average_mark = total_marks / num_reviews if num_reviews != 0 else 0
    
    
    context = {
        'product': product,
        'average_mark':average_mark,
        'rating':range(1,6),
        'categories':categories,
    }
    
    return render(request, 'shop-detail.html', context)
