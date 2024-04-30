
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('shop/', views.shop, name="shop")
]