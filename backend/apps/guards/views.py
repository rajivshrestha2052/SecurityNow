from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.accounts.permissions import IsGuard
from .models import GuardProfile
from .serializers import GuardProfileSerializer


class GuardProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = GuardProfileSerializer
    permission_classes = [IsGuard]

    def get_object(self):
    
        return GuardProfile.objects.get(
            user=self.request.user
        )


class GuardAvailabilityView(generics.UpdateAPIView):
    serializer_class = GuardProfileSerializer
    permission_classes = [IsGuard]

    def get_object(self):
        return GuardProfile.objects.get(
            user=self.request.user
        )

    def update(self, request, *args, **kwargs):
        profile = self.get_object()

        if "is_available" not in request.data:
            return Response(
                {
                    "detail": "is_available is required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        profile.is_available = request.data["is_available"]

        profile.save(
            update_fields=["is_available"]
        )

        return Response(
            self.get_serializer(profile).data
        )