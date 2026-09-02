from django.urls import path

from .views import (
    GuardProfileView,
    GuardAvailabilityView,
)


urlpatterns = [
    path(
        "profile/",
        GuardProfileView.as_view(),
        name="guard-profile",
    ),
    path(
        "availability/",
        GuardAvailabilityView.as_view(),
        name="guard-availability",
    ),
]