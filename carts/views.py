from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from products.models import Product
from .models import Cart
from .serializer import CartSerializer

class CartView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Cart.objects.filter(user_id=pk)

    def perform_create(self, serializer):
        cart_products = Cart.objects.all()
        for cart_product in cart_products:
                stock = cart_product.stock
                quantity = cart_product.quantity
                if stock < quantity:
                    raise serializer.ValidationError(f"Insufficient stock for product '{cart_product.name}'")
                stock -= quantity
                cart_product.save()

        return cart_products
    

    
  

        

 