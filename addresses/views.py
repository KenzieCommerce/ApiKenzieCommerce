from rest_framework import generics
from .serializers import AddressSerializer
from .models import Address


# class AddressView(generics.CreateAPIView):
#     serializer_class: AddressSerializer
#     model: Address
