from rest_framework import serializers
from .models import Address

   
class AddresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street_name', 'city', 'number', 'zip_code',]