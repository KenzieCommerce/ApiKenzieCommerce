from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "category", "stock", "available", "price", "user"]
        extra_kwargs = {"user": {"read_only": True}}

    def create(self, validated_data):
        # user = validated_data.pop("user")

        user = self.context["request"].user

        if validated_data.get("stock", 0) > 0:
            validated_data["available"] = True
        else:
            validated_data["available"] = False

        product = Product.objects.create(user=user, **validated_data)
        return product
