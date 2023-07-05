from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "category", "stock", "available", "price", "user"]
        extra_kwargs = {"user": {"read_only": True}}

    def create(self, validated_data):
        # user = validated_data.pop("user")

        if validated_data.get("stock", 0) > 0:
            validated_data["available"] = True
        else:
            validated_data["available"] = False

        return Product.objects.create(**validated_data)
