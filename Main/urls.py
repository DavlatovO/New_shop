
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('shop/', views.shop, name="shop"),
    path('shop-detail/<slug:slug>/', views.shop_detail, name='shop_detail'),

]