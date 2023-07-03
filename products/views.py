from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class ProductDeatilView(generics.RetrieveUpdateDestroyAPIView):
    ...