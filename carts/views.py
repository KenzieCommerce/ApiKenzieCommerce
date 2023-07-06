from rest_framework import generics
from rest_framework.views import  Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.models import Product
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartProducts
from django.shortcuts import get_object_or_404
from .permissions import IsSuperUser
from .serializer import CartSerializer, CartProductSerializer, CartListSerializer


class ListCartView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CartListSerializer

    def get_queryset(self):
        cart = get_object_or_404(Cart.objects.filter(user=self.request.user))
        cart_products = CartProducts.objects.filter(cart=cart)
        return cart_products
    

class CartDetailView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CartProducts.objects.all()
    serializer_class = CartProductSerializer

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        cart = get_object_or_404(Cart.objects.filter(user=request.user))
        cart_products = get_object_or_404(CartProducts.objects.filter(cart=cart))
        product = get_object_or_404(Product, pk=pk)
        if product in cart_products.products.all():
            cart_products.products.remove(product)
        cart_products.save()
        return Response( {"message": "Produto deletado com sucesso."},
                         status=status.HTTP_204_NO_CONTENT)
    
