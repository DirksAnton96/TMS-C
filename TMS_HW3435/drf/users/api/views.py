from .serializers import UserListSerializer, UserCreateSerializer
from users.models import User
from rest_framework import permissions, viewsets
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import MethodNotAllowed


class UserViewSet(ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    def get_serializer_class(self):
         if self.request.method == 'POST':
             return UserCreateSerializer
         elif self.request.method == 'GET' and self.request.user.is_superuser:
             permission_classes = [permissions.IsAdminUser]
             return UserListSerializer
         else :
             raise MethodNotAllowed(f"Метод {self.request.method} не поддерживается")
         
    def perform_create(self, serializer):
        data = serializer.validated_data
        password = make_password(data.get('password'))
        serializer.save(password=password)
        
        
        
