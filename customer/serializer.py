from rest_framework import serializers
from .models import CustomUser
from hashed import hash_password

MIN_LENGHT = 8

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only = True,
        min_length = MIN_LENGHT,
        error_messages = {
            "min_length": f"Password must be {MIN_LENGHT} characters long"
        }
    )
    password2 = serializers.CharField(
        write_only = True,
        min_length = MIN_LENGHT,
        error_messages = {
            "min_length": f"Password must be {MIN_LENGHT} characters long"
        }
    )

    class Meta:
        model = CustomUser
        exclude = ['groups', 'user_permissions', 'is_staff', 'is_superuser', 'last_login', 'date_joined']

    # data validation
    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match")
        return data
    
    # saving validated data
    def create(self, validated_data):
        hashed = hash_password(validated_data["password"], validated_data["password2"])

        user = CustomUser.objects.create(
            username = validated_data["username"],
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
            email = validated_data["email"]
        )
        user.set_password(hashed)

        # saving new user
        user.save()

        return user
    
class CustomerLoginAPI(serializers.ModelSerializer):
    pass