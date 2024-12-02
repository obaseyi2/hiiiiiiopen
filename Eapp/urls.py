from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

from django.contrib import admin

app_name = 'Eapp'

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('ping', views.ping, name='ping'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('headgear', views.headgear, name='headgear'),
    path('home', views.home, name='home'),
    path('beauty', views.beauty, name='beauty'),
    path('computers', views.computers, name='computers'),
    path('electronics', views.electronics, name='electronics'),
    path('faqs', views.faqs, name='faqs'),
    path('food', views.food, name='food'),
    path('jewelry', views.jewelry, name='jewelry'),
    path('shop', views.shop, name='shop'),
    path('sell', views.sell, name='sell'),
    path('error', views.error, name='error'),
    path('footwear', views.footwear, name='footwear'),
    path('bags', views.bags, name='bags'),
    path('apparel', views.apparel, name='apparel'),
    path('vendor', views.vendor, name='vendor'),
    path('login', views.user_login, name='login'),
    path('register', views.register, name='register'),
    path('logout', auth_views.LogoutView.as_view(next_page='Eapp:login'), name='logout'),
]