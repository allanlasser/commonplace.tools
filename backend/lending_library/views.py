from django.shortcuts import render
from lending_library.models import Location, Network, LendableStatus, LendableType
from lending_library.models import Lendable, Loan, UserProfile 
from django.contrib.auth.models import User, Group, Permission
from lending_library.serializers import GroupSerializer, PermissionSerializer, UserSerializer, LoanSerializer, LocationSerializer, NetworkSerializer, LendableSerializer, LendableTypeSerializer, LendableStatusSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from lending_library.permissions import IsOwnerOrReadOnly
from rest_framework.viewsets import ModelViewSet

class LocationViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly,]
    queryset = Location.objects.all().order_by('id')
    serializer_class = LocationSerializer

class NetworkViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Network.objects.all().order_by('id')
    serializer_class = NetworkSerializer

class LendableTypeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = LendableType.objects.all().order_by('id')
    serializer_class = LendableTypeSerializer

class LendableStatusViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = LendableStatus.objects.all().order_by('id')
    serializer_class = LendableStatusSerializer

class LendableViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Lendable.objects.all().order_by('id')
    serializer_class = LendableSerializer

class LoanViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Loan.objects.all().order_by('id')
    serializer_class = LoanSerializer

class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class GroupViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer

class PermissionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Permission.objects.all().order_by('id')
    serializer_class = PermissionSerializer