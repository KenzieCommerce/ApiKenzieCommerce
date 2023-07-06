from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwnerAdmin, IsEmployee
from rest_framework.permissions import IsAdminUser


class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer

    # queryset = User.objects.all()


class UserListAdmView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self, request, *args, **kwargs):
        print(self)
        return super().get(request, *args, **kwargs)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerAdmin]

    serializer_class = UserSerializer
    queryset = User.objects.all()
