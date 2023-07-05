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

    def update(self, instance, validated_data):
        address_data = validated_data.pop("address", None)
        if address_data:
            address_serializer = AddressSerializer(data=address_data, partial=True)
            address_serializer.is_valid(raise_exception=True)
            address_serializer.save(user=instance)

            print(instance.__dict__)
            # TENHO QUE PEGAR, O USER ADMIN PELO TOKEN 
        if instance.is_superuser == True:
            for key, value in validated_data.items():
                if key == "password":
                    instance.set_password(value)
                else:
                    setattr(instance, key, value)

                instance.save()
        else:
            for key, value in validated_data.items():
                if key == "password":
                    instance.set_password(value)
                elif key == "is_superuser":
                    key == instance.is_superuser
                else:
                    setattr(instance, key, value)

                instance.save()

        return instance


class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "is_employee",
            "is_superuser",
        ]
