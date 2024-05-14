from django.shortcuts import render, get_object_or_404
from . import models
from django.contrib.auth.decorators import login_required

# @login_required(login_url='auth:login')

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

############################################################################################

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from . forms import SignupForm, LoginForm


# Create your views here.
# Home page


# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'auth/register.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')




