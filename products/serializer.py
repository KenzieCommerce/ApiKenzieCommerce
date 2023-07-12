from rest_framework import serializers
from .models import Product
from decimal import Decimal


class ProductSerializer(serializers.ModelSerializer):
    seller_name = serializers.CharField(source="user", read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "stock",
            "image",
            "available",
            "price",
            "discount_vouchers",
            "seller_name",
        ]
        extra_kwargs = {"seller_name": {"read_only": True}}

    def create(self, validated_data):
       
        user = self.context["request"].user
        discount_vouchers = validated_data.get("discount_vouchers") # método get() para obter o valor ou None
    

        if discount_vouchers:
            if validated_data["discount_vouchers"] == "10% OFF":
                validated_data["price"] = Decimal(validated_data["price"]) * Decimal(0.9)
            elif validated_data["discount_vouchers"] == "25% OFF":
                validated_data["price"] = Decimal(validated_data["price"]) * Decimal(0.75)
            elif validated_data["discount_vouchers"] == "80% OFF":
                validated_data["price"] = Decimal(validated_data["price"]) * Decimal(0.2)

        if validated_data.get("stock", 0) > 0:
            validated_data["available"] = True
        else:
            validated_data["available"] = False

        product = Product.objects.create(user=user, **validated_data)
        return product


class ReadProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "category", "price", "available"]
