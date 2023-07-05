from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwnerAdmin, IsEmployee


class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer

    # queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerAdmin]

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserProductsView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee, IsAccountOwnerAdmin]

    serializer_class = UserSerializer
    queryset = User.objects.all()
