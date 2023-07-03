from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator
from addresses.serializers import AddressSerializer


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    address = AddressSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "is_employee",
            "is_superuser",
            "date_joined",
            "updated_at",
            "address",
        ]
