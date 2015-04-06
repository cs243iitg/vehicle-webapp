from rest_framework import permissions

class IsReporter(permissions.BasePermission):
    """
        Permission allowing reporters to access their own reports
        
    """

    def has_object_permission(self, request, view, obj):
       
        return obj.reporter == request.user