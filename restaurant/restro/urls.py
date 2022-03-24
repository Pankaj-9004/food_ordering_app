from django.contrib import admin
from django.urls import path
from . views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('homepage/', homepage),
    path('signup/', signup),
    path('signin/', signin),
    path('signout/', signout),
    path('profile/', profile),
    path('update_profile/', update_profile),
    path('meal_detail/<int:pk>/', meal_detail, name='meal_detail'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),

    path('add/<int:id>/', cart_add, name='cart_add'),
    path('item_clear/<int:id>/', item_clear, name='item_clear'),
    path('item_increment/<int:id>/', item_increment, name='item_increment'),
    path('item_decrement/<int:id>/', item_decrement, name='item_decrement'),
    path('cart_clear/', cart_clear, name='cart_clear'),
    path('cart_detail/', cart_detail, name='cart_detail'),
    path('checkout/', checkout, name='checkout'),
    path('payment/', payment, name='payment'),
]
