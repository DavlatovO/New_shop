from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('log-in/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
]