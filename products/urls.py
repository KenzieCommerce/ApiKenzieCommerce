from django.urls import path
from .views import ProductDeatilView, ProductView

urlpatterns = [
    path("products/", ProductView.as_view()),
    path("products/<int:product_id>/", ProductDeatilView.as_view())
]