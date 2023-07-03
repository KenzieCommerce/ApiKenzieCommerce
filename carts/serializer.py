from rest_framework import serializers
from models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "user_id", "products"]
        extra_kwargs = {"user_id": {"read_only": True}, "products": {"read_only": True}}
