from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "admin"

class IsEditor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "editor"

class IsViewer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "viewer"
