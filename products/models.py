from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=40)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        related_name="product"
    )

    order = models.ManyToManyField(
        "orders.Order",
        related_name="products"
    )

