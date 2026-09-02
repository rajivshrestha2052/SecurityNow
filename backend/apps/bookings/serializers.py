from rest_framework import serializers

from .models import Booking, BookingApplication


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "id",
            "title",
            "description",
            "address",
            "latitude",
            "longitude",
            "start_datetime",
            "end_datetime",
            "guards_required",
            "status",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "status",
            "created_at",
            "updated_at",
        )

    def validate(self, data):
        start_datetime = data.get("start_datetime")
        end_datetime = data.get("end_datetime")
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        
        if start_datetime and end_datetime:
            if end_datetime <= start_datetime:
                raise serializers.ValidationError(
                    {
                        "end_datetime": (
                            "End date and time must be after "
                            "the start date and time."
                        )
                    }
                )

        if latitude is not None:
            if latitude < -90 or latitude > 90:
                raise serializers.ValidationError(
                    {
                        "latitude": "Latitude must be between -90 and 90."
                    }
                )

        if longitude is not None:
            if longitude < -180 and longitude > 180:
                raise serializers.ValidationError(
                    {
                        "longitude": "Longitude must be between -180 and 180"
                    }
                )

        return data

class BookingApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingApplication
        fields = (
            "id",
            "booking",
            "message",
            "status",
            "created_at",
        )

        read_only_fields = (
            "id",
            "booking",
            "status",
            "created_at",
        )

    def validate(self, attrs):
        request = self.context["request"]
        booking_id = self.context["view"].kwargs["booking_id"]

        if BookingApplication.objects.filter(
            booking_id=booking_id,
            guard=request.user,
        ).exists():
            raise serializers.ValidationError(
                {
                    "detail": "You have already applied for this booking."
                }
            )

        return attrs

class BookingApplicationDetailSerializer(serializers.ModelSerializer):
    guard_id = serializers.IntegerField(
        source="guard.id",
        read_only=True,
    )
    guard_username = serializers.CharField(
        source="guard.username",
        read_only=True,
    )

    class Meta:
        model = BookingApplication
        fields = (
            "id",
            "guard_id",
            "guard_username",
            "message",
            "status",
            "created_at",
        )