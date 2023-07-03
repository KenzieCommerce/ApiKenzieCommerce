from django.db import models


class Status(models.TextChoices):
    ANDAMENTO = "ANDAMENTO"
    REALIZADO = "REALIZADO"
    ENTREGUE = "ENTREGUE"


class Order(models.Model):
    status = models.CharField(
        choices=Status.choices, max_length=20, default=Status.REALIZADO
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="order"
    )
