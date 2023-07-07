from rest_framework import serializers
from .models import Cart,CartProducts
from products.serializer import ProductSerializer
from products.models import Product
from rest_framework import status

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProducts
        fields = ["id", "cart","product"]
        read_only_fields = ["cart"]

    def create(self,validated_data):
        item,_created = Cart.objects.get_or_create(user=validated_data["user"])
        product = validated_data["product"]
        Cart_products = CartProducts.objects.filter(cart=item,product=validated_data["product"]).first()

        if product.stock <= 0:
            raise serializers.ValidationError("O produto não está em estoque.")

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
        extra_kwargs = {"user": {"read_only": True}, "products": {"read_only": True}}
        

    def update(self, instance, validated_data):
        remove_product_id=self._kwargs["data"]["remove_product_id"]
        if remove_product_id :
            get_product = Product.objects.filter(id=remove_product_id).first()
            instance.products.remove(get_product)
            instance.save()
            return instance
        
        product_id=self._kwargs["data"]["product_id"]
        get_product = Product.objects.filter(id=product_id).first()
        instance.products.add(get_product)
        instance.save()
        return instance