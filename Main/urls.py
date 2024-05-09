
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('shop/', views.shop, name="shop"),
    path('shop-detail/<slug:slug>/', views.shop_detail, name='shop_detail'),
    path('log-in/', include('auth.urls')),
    path('log-in/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
]

