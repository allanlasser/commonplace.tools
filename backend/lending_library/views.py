from django.shortcuts import render
from lending_library.models import Location, Network, LendableStatus, LendableType
from lending_library.models import Lendable, Loan, UserProfile 
from django.contrib.auth.models import User, Group, Permission
from lending_library.serializers import GroupSerializer, PermissionSerializer, UserSerializer, LoanSerializer, LocationSerializer, NetworkSerializer, LendableSerializer, LendableTypeSerializer, LendableStatusSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class NetworkViewSet(ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer

class LendableTypeViewSet(ModelViewSet):
    queryset = LendableType.objects.all()
    serializer_class = LendableTypeSerializer

class LendableStatusViewSet(ModelViewSet):
    queryset = LendableStatus.objects.all()
    serializer_class = LendableStatusSerializer

class LendableViewSet(ModelViewSet):
    queryset = Lendable.objects.all()
    serializer_class = LendableSerializer

class LoanViewSet(ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PermissionViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer