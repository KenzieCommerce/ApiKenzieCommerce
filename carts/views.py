from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.models import Product
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartProducts
from django.shortcuts import get_object_or_404
from .permissions import IsOwnerOrAdm
from .serializer import CartSerializer, CartListSerializer


class ListCartView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CartListSerializer

    def get_queryset(self):
        cart = get_object_or_404(Cart.objects.filter(user=self.request.user))
        cart_products = CartProducts.objects.filter(cart=cart)
        return cart_products


class CartAddRemoveProductView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdm]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
