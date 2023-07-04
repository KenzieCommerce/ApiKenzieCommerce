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
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        address_data = validated_data.pop("address")
        user = User.objects.create_user(**validated_data)
        address_serializer = AddressSerializer(data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address_serializer.save(user=user)
        return user
