from rest_framework.permissions import BasePermission

class IsCustomer(BasePermission):
    message = "Only Customers can access this resource."

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "CUSTOMER"
        )

class IsGuard(BasePermission):
    message = "Only guards can access this resource."

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "GUARD"
        )