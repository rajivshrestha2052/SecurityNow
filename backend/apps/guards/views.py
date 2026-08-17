from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from .models import GuardProfile
from .serializers import GuardProfileSerializer


class GuardProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = GuardProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        if self.request.user.role != "GUARD":
            raise PermissionDenied(
                "Only guards can access this profile."
            )

        return GuardProfile.objects.get(
            user=self.request.user
        )