from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from users.views import UserView
from .views import CartView

urlpatterns = [
    path("users/cart/", views.CartView.as_view()),
    path("users/cart/", views.ListCartView.as_view()),
    path("users/<int:pk>/cart/", views.CartDetailView.as_view()),
   
]