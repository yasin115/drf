from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_superuser


class UserAccessPermission(BasePermission):
    """
    - staff: فقط دیدن
    - superuser: همه‌چی
    - user عادی: هیچ
    """

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        if user.is_staff and view.action in ["list", "retrieve"]:
            return True

        return False


class ArticlePermission(BasePermission):
    """
    - همه: read
    - staff: create + edit فقط مال خودش
    - superuser: full access
    """

    def has_permission(self, request, view):
        user = request.user

        if request.method in SAFE_METHODS:
            return True

        if not user or not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        if user.is_staff and view.action == "create":
            return True

        return False

    def has_object_permission(self, request, view, obj):
        user = request.user

        if request.method in SAFE_METHODS:
            return True

        if user.is_superuser:
            return True

        if user.is_staff and obj.author == user:
            return True

        return False