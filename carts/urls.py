from django.urls import path
from .views import CartAddRemoveProductView

urlpatterns = [
    path("users/cart/<int:pk>/", CartAddRemoveProductView.as_view()),
]
