from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "category", "stock", "available", "price", "user"]
        extra_kwargs = {"user": {"read_only": True}}

    def create(self, validated_data):
        return super().create(**validated_data)
