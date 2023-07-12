from django.db import models
from django.contrib.postgres.fields import ArrayField


class DiscountVouchers(models.TextChoices):
    OFF10 = "10% OFF"
    OFF25 = "25% OFF"
    OFF80 = "80% OFF"


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=40)
    stock = models.PositiveIntegerField()
    image = ArrayField(models.TextField())
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_vouchers = models.CharField(
        max_length=25, choices=DiscountVouchers.choices,null=True, default=None
    )

    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="product"
    )

    order = models.ManyToManyField("orders.Order", related_name="products")
