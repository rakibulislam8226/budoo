from rest_framework.permissions import BasePermission


class IsAdminOrSelf(BasePermission):
    """
    Custom permission to only allow admin users or the user themselves to access or modify user details.
    """

    def has_object_permission(self, request, view, obj):
        return True if request.user and request.user.is_staff else request.user == obj
