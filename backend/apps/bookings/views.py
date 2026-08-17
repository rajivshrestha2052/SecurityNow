from rest_framework import generics

from apps.accounts.permissions import IsCustomer, IsGuard
from .models import Booking
from .serializers import (
    BookingSerializer,
    BookingApplicationSerializer,
    BookingApplicationDetailSerializer,
)
from django.shortcuts import get_object_or_404

class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsCustomer]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class AvailableBookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsGuard]

    def get_queryset(self):
        return Booking.objects.filter(
            status=Booking.Status.PENDING
        ).order_by("start_datetime")


class BookingApplyView(generics.CreateAPIView):
    serializer_class = BookingApplicationSerializer
    permission_classes = [IsGuard]

    def perform_create(self, serializer):
        booking_id = self.kwargs["booking_id"]

        booking = get_object_or_404(
            Booking,
            id=booking_id,
            status=Booking.Status.PENDING,
        )

        serializer.save(
            booking=booking,
            guard=self.request.user,
        )

class BookingApplicationListView(generics.ListAPIView):
    serializer_class = BookingApplicationDetailSerializer
    permission_classes = [IsCustomer]

    def get_queryset(self):
        booking = get_object_or_404(
            Booking,
            id=self.kwargs["booking_id"],
            customer=self.request.user,
        )

        return booking.applications.select_related(
            "guard"
        ).order_by("-created_at")