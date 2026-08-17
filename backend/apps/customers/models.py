from django.db import models
from django.conf import settings

class CustomerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="customer_profile"
        )
    company_name = models.CharField(
        max_length=255,
        blank = True,
    )
    address = models.TextField(
        blank= True
    )
    created_at = models.DateField(
        auto_now_add=True,
    )
    updated_at = models.DateField(
        auto_now=True,
    )

    def __str__(self):
        return f"Customer: {self.user.username}"