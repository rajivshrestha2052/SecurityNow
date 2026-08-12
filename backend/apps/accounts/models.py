from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        GUARD = "GUARD", "Guard"

    role = models.CharField(
        max_length=20,
        choices= Role.choices,
    )
    phone_number = models.CharField(
        max_length=15,
        unique= True,
    )

    def _str_(self):
        return f"{self.username} ({self.role}"

