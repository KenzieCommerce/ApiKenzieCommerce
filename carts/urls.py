from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from users.views import UserView
from carts.views import ListCartView, CartDetailView

urlpatterns = [
    path("users/cart/", ListCartView.as_view()),
    path("users/cart/<int:pk>/remove/", CartDetailView.as_view()),
   
]