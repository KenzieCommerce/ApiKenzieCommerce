from django.db import models


class Cart(models.Model):
    products = models.ManyToManyField(
        "products.Product", related_name="cart_products", through="carts.CartProducts"
    )
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="cart"
    )


class CartProducts(models.Model):
    class Meta:
        ordering = ["id"]

    cart = models.ForeignKey(
        "carts.Cart", on_delete=models.CASCADE, related_name="cart_pivo"
    )

    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="product_pivo"
    )
    # quantity = models.PositiveIntegerField(default=1)
