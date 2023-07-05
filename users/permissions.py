from rest_framework import permissions
from .models import User
from rest_framework.views import View


class IsAccountOwnerAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User):
        if request.user.is_superuser:
            return True
        return request.user.is_authenticated and obj == request.user


class IsEmployee(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User):
        print(request.user.is_employee)
        if request.user.is_employee or request.user.is_superuser:
            return True
