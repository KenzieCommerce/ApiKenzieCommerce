from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from .views import UserView

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
]
