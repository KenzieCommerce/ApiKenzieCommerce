from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from users.views import UserView
from .views import ListCartView, CartDestroyView, CartAddProductView

urlpatterns = [
    path("users/cart/", ListCartView.as_view()),
    path("users/cart/<int:pk>/", CartAddProductView.as_view()),
    path("users/cart/<int:pk>/remove/", CartDestroyView.as_view()), 
]