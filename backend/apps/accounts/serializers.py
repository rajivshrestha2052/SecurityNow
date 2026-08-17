from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.customers.models import CustomerProfile
from apps.guards.models import GuardProfile
from django.db import transaction
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "phone_number",
            "password",
            "role",
        )

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Email Already Exists"
            )
        return value

    def validate_phone_number(self, value):
            if User.objects.filter(phone_number=value).exists():
                raise serializers.ValidationError(
                    "Phone number Already Exists"
                )
            return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        with transaction.atomic():
            user = User(**validated_data)
            user.set_password(password)
            user.save()

            if user.role == User.Role.CUSTOMER:
                CustomerProfile.objects.create(user=user)
            elif user.role == User.Role.GUARD:
                GuardProfile.objects.create(user=user)

        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data["role"] = self.user.role
        data["user_id"] = self.user.id
        return data

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "phone_number",
            "password",
            "role",
        )
        read_only_fields = fields
        