from rest_framework import serializers
from .models import Cart,CartProducts
from products.serializer import ProductSerializer
from products.models import Product

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProducts
        fields = ["id", "cart","product"]
        read_only_fields = ["cart"]

    def create(self,validated_data):
        item,_created = Cart.objects.get_or_create(user=validated_data["user"])
        Cart_products = CartProducts.objects.filter(
            cart=item,product=validated_data["product"]
            

        ).first()

        validated_data.pop("user",None) 
        return CartProducts.objects.create(cart=item,**validated_data)

class CartListSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartProducts
        fields = ["id", "cart","product"]
        read_only_fields = ["cart"]


class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ["id", "user", "products"]

    def update(self, instance, validated_data):
        product_id=self._kwargs["data"]["product_id"]
        get_product = Product.objects.filter(id=product_id).first()
        instance.products.add(get_product)
        instance.save()
        return instance