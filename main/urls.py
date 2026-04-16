from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home,name='home'),
    path('', views.splash),
    path('add/<int:id>/',views.add_to_cart,name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
]