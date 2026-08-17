from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import CustomerProfile
from .serializers import CustomerProfileSerializer

class CustomerProfileView(generics.RetrieveAPIView):
    serializer_class = CustomerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        if self.request.user.role != "CUSTOMER":
            raise PermissionDenied(
                "This profile is not Authorized to access. Only Customer."
            )
        return CustomerProfile.objects.get(
            user=self.request.user
        )