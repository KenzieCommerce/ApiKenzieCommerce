from rest_framework import serializers
from .models import Order
from users.serializers import UserReturnSerializer
from products.serializer import ReadProductsSerializer


class OrderSerializer(serializers.ModelSerializer):
    user = UserReturnSerializer(read_only=True)
    products = ReadProductsSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "status", "created_at", "updated_at", "user", "products"]
        read_only_fields = ["created_at", "updated_at", "user", "products"]

    def create(self, validated_data):
        result = super().create(validated_data)
        products = validated_data["user"].cart.products.all()
        cart = validated_data["user"].cart

        for product in products:
            if product.stock == 0:
                cart.products.clear()
                raise serializers.ValidationError(
                    {"msg": "o produto não está mais disponível"}
                )
            product.stock -= 1
            product.save()
            result.products.add(product)

        cart.products.clear()
        return result
