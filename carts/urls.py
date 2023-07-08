from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from users.views import UserView
from .views import ListCartView, CartAddRemoveProductView

urlpatterns = [
    path("users/cart/", ListCartView.as_view()),
    path("users/cart/<int:pk>/", CartAddRemoveProductView.as_view()),
]
