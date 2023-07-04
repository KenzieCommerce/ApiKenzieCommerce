from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from users.views import UserView
from .views import CartView

urlpatterns = [
    path("users/<int:pk>/cart/", views.CartView.as_view()),
   
]