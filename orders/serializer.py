from rest_framework import serializers
from .models import Order
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from users.models import User


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ["id", "status", "created_at", "updated_at", "user"]
        read_only_fields = ["created_at", "updated_at", "user"]

    def create(self, validated_data):
        result = super().create(validated_data)
        products = validated_data["user"].cart.products.all()

        for product in products:
            product.stock -= 1
            product.save()
            result.products.add(product)
        return result
