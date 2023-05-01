from rest_framework.permissions import BasePermission


class RadiusPermission(BasePermission):
    def has_permission(self, request, view):
        if request.META.get('HTTP_NAME') == 'Radius':
            return True
        return False
