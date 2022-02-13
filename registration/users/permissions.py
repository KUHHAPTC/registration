from rest_framework import permissions


class IsEmailVerified(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.email_verified:
            return True
        return False