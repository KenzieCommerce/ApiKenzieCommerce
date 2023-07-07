from rest_framework import generics
from rest_framework.views import  Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.models import Product
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartProducts
from django.shortcuts import get_object_or_404
from .permissions import IsSuperUser
from .serializer import CartSerializer, CartProductSerializer, CartListSerializer
from users.models import User


class ListCartView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CartListSerializer

    def get_queryset(self):
        cart = get_object_or_404(Cart.objects.filter(user=self.request.user))
        cart_products = CartProducts.objects.filter(cart=cart)
        return cart_products


 
    
class CartAddProductView(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# TENTAR FAZER COM A MODEL DE USER E PEGAR O CART PELO ID
