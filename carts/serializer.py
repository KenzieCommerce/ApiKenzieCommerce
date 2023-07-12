from rest_framework import serializers
from .models import Cart, CartProducts
from products.serializer import ProductSerializer
from products.models import Product


class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "products"]
        extra_kwargs = {"user": {"read_only": True}, "products": {"read_only": True}}

    def update(self, instance, validated_data):
        remove_product_id = self._kwargs["data"]["remove_product_id"]
        if remove_product_id:
            get_product = Product.objects.filter(id=remove_product_id).first()
            instance.products.remove(get_product)
            instance.save()
            return instance

        product_id = self._kwargs["data"]["product_id"]
        get_product = Product.objects.filter(id=product_id).first()
        instance.products.add(get_product)
        instance.save()
        return instance
