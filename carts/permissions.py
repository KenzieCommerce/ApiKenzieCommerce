from rest_framework import permissions
from users.models import User
from rest_framework.views import View
from users.models import User

class IsSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User):
       
        return obj == request.user or request.user.is_superuser  
    
class IsOwnerOrAdm(permissions.BasePermission):
    def has_object_permission(self, request, view, obj:User):
        print(obj.user_id)
        print(request.user.id)

        get_user = User.objects.get(id = request.user.id)

        return obj.user_id == request.user.id or get_user.is_superuser == True