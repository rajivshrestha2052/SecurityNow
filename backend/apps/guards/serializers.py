from rest_framework import serializers

from .models import GuardProfile, GuardLocation


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
            "current_latitude",
            "current_longitude",
            "location_updated_at",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "verification_status",
            
            "current_latitude",
            "current_longitude",
            "location_updated_at",
            "created_at",
            "updated_at",
        )

class GuardLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuardLocation
        fields = (
            "id",
            "guard",
            "booking",
            "latitude",
            "longitude",
            "recorded_at",
        )

        read_only_fields = (
            "id",
            "guard",
            "recorded_at",
        )

    def validate(self, data):
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        if latitude < -90 or latitude > 90:
            raise serializers.ValidationError(
                {
                    "latitude": (
                        "Latitude must be between -90 and 90."
                    )
                }
            )

        if longitude < -180 or longitude > 180:
            raise serializers.ValidationError(
                {
                    "longitude": (
                        "Longitude must be between -180 and 180."
                    )
                }
            )

        return data