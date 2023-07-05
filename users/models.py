from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_employee = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)

  
    address = models.OneToOneField(
        "addresses.Address",
        on_delete=models.CASCADE,
        related_name="user",
        null=True
    )