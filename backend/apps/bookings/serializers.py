from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "id",
            "title",
            "description",
            "location",
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

        return data