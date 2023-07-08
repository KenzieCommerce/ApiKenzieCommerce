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

    # def create(self, validated_data):
    #     print(self.get_attribute)
    #     user = get_object_or_404(User, username=validated_data["user"])
    #     return super().create(validated_data)
