from rest_framework import generics
from apps.accounts.permissions import IsCustomer
from .models import CustomerProfile
from .serializers import CustomerProfileSerializer

class CustomerProfileView(generics.RetrieveAPIView):
    serializer_class = CustomerProfileSerializer
    permission_classes = [IsCustomer]

    def get_object(self):
        
        return CustomerProfile.objects.get(
            user=self.request.user
        )