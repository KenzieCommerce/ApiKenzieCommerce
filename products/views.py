from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAccountOwnerAdmin, IsEmployee
from .filters import ProductFilter


class ProductView(generics.ListCreateAPIView):
    permission_classes = [IsAccountOwnerAdmin, IsEmployee]
    authentication_classes=[JWTAuthentication]
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def get_queryset(self):
        queryset = Product.objects.all()
        queryset = self.filterset_class(self.request.GET, queryset=queryset).qs
        return queryset


    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ProductDeatilView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Product.objects.filter(pk=product_id)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
