from django.db import models

class Cart(models.Model):
    products = models.ManyToManyField(
        "products.Product",
        related_name="cart"
    )