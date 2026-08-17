from rest_framework import generics
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