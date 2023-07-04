from django.shortcuts import render
from rest_framework import generics
from .models import Order
from .serializer import OrderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser
from .permissions import IsOrderOwner


# Create your views here.
class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser | IsOrderOwner]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
