from rest_framework import serializers
from .models import Order
from users.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Order
        fields = ["id", "status", "created_at", "updated_at", "user"]
        read_only_fields = ["created_at", "updated_at", "user"]
