from rest_framework import serializers

from .models import GuardProfile


class GuardProfileSerializer(serializers.ModelSerializer):
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
        model = GuardProfile

        fields = (
            "username",
            "email",
            "phone_number",
            "verification_status",
            "experience_years",
            "bio",
            "is_available",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "verification_status",
            "created_at",
            "updated_at",
        )