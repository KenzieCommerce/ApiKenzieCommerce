from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Cart
from .permissions import IsOwnerOrAdm
from .serializer import CartSerializer


class CartAddRemoveProductView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdm]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
