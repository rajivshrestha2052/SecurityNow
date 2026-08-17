from rest_framework import serializers
from .models import CustomerProfile

class CustomerProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        source="user.username",
        read_only=True,
    )
    email = serializers.EmailField(
        source="user.email",
        read_only=True,
    )
    phone_number = serializers.CharField(
        source="user.phone_number",
        read_only=True,
    )

    class Meta:
        model = CustomerProfile
        fields = (
            "username",
            "email",
            "phone_number",
            "company_name",
            "address",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )