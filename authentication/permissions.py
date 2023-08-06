from rest_framework import permissions


class IsAdmAccount(permissions.BasePermission):
    message = 'Just adm account are allowed to perform requested action'

    def has_permission(self, request, view):
        if bool(request.user.account and request.user.account.is_company_admin):
            return True
        return False
