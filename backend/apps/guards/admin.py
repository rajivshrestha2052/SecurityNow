from django.contrib import admin

from .models import GuardProfile, GuardLocation

@admin.register(GuardProfile)
class GuardProfileAdmin(admin.ModelAdmin):
    list_display=(
        "user",
        "verification_status",
        "is_available",
        "experience_years",
        "created_at",
    )
    list_filter=(
        "verification_status",
        "is_available",
    )
    search_fields=(
        "user__username",
        "user__email",
        "user__phone_number",
    )
    readonly_fields=(
        "created_at",
        "updated_at",
    )

@admin.register(GuardLocation)
class GuardLocationAdmin(admin.ModelAdmin):
    list_display = (
        "guard",
        "booking",
        "latitude",
        "longitude",
        "recorded_at",
    )

    list_filter = (
        "recorded_at",
    )

    search_fields = (
        "guard__user__username",
        "guard__user__email",
    )

    readonly_fields = (
        "recorded_at",
    )