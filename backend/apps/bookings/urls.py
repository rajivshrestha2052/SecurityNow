from django.urls import path

from .views import (
    BookingCreateView,
    AvailableBookingListView,
    BookingApplyView,
    BookingApplicationListView
)


urlpatterns = [
    path(
        "",
        BookingCreateView.as_view(),
        name="booking-create",
    ),
    path(
        "available/",
        AvailableBookingListView.as_view(),
        name="available-bookings",
    ),

    path(
        "<int:booking_id>/apply/",
        BookingApplyView.as_view(),
        name="booking-apply",
    ),
    path(
    "<int:booking_id>/applications/",
    BookingApplicationListView.as_view(),
    name="booking-applications",
    ),
]