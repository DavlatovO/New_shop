
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('shop/', views.shop, name="shop"),
    path('shop-detail/<slug:slug>/', views.shop_detail, name='shop_detail'),
    path('log-in/',views.user_login, name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('signup/',views.user_signup,name='signup'),
   
   ]

