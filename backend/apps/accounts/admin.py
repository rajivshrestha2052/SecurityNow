from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .actions import deactivate_guards, mark_as_guard
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
        "SecurityNow Information",
        {
            "fields":(
                "role",
                "phone_number",
            )
        },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
        "SecurityNow Information",
        {
            "fields":(
                "role",
                "phone_number",
            )
        },
        ),
    )

    list_display = (
        "username",
        "email",
        "phone_number",
        "role",
        "is_active",
        "is_staff",
    )

    list_filter = (
        "role",
        "is_active",
        "is_staff",
    )

    actions = [deactivate_guards, mark_as_guard]