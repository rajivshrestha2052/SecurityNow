from django.conf import settings
from django.db import models

class GuardProfile(models.Model):
    
    class VerificationStatus(models.TextChoices):
        PENDING = "PENDING", "Pending"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="guard_profile",
    )

    verification_status = models.CharField(
        max_length=20,
        choices=VerificationStatus.choices,
        default=VerificationStatus.PENDING,
    )

    experience_years = models.PositiveIntegerField(
        default=0,
    )

    bio = models.TextField(
        blank=True,
    )

    is_available = models.BooleanField(
        default=False,
    )
    
    current_latitude = models.DecimalField(
    max_digits=9,
    decimal_places=6,
    null=True,
    blank=True,
    )

    current_longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )

    location_updated_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"Guard: {self.user.username}"


class GuardLocation(models.Model):
    guard = models.ForeignKey(
        GuardProfile,
        on_delete=models.CASCADE,
        related_name="locations",
    )

    booking = models.ForeignKey(
        "bookings.Booking",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="guard_locations",
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
    )

    recorded_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-recorded_at"]
        indexes = [
            models.Index(
                fields=["guard", "-recorded_at"]
            ),
            models.Index(
                fields=["booking", "-recorded_at"]
            ),
        ]

    def __str__(self):
        return (
            f"{self.guard.user.username} - "
            f"{self.latitude}, {self.longitude}"
        )