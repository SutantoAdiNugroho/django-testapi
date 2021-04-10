from django.contrib.auth.models import  User, Group # Model (database)
from rest_framework import viewsets, permissions # CRUD with permissions
from APITest.serializers import UserSerializer, GroupSerializer # Template (front-end)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer # sync querysets
    permission_classes = [permissions.IsAuthenticated] # no one can take except the autenticated user

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]