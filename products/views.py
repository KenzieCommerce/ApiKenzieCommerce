from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProductView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ProductDeatilView(generics.RetrieveUpdateDestroyAPIView):
    ...
