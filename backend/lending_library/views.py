from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter
from lending_library.models import Location, Network, LendableStatus, LendableType
from lending_library.models import Lendable, Loan, UserProfile
from lending_library.serializers import GroupSerializer, PermissionSerializer, UserSerializer
from lending_library.serializers import LoanSerializer, LocationSerializer, NetworkSerializer, ContentTypeSerializer
from lending_library.serializers import LendableSerializer, LendableTypeSerializer, LendableStatusSerializer
from lending_library.permissions import IsOwnerOrReadOnly


class LocationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Location.objects.all().order_by('id')
    serializer_class = LocationSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('name',)
    filterset_fields = ['name', 'address1', 'address2', 'city', 'state', 'postal_code']


class NetworkViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Network.objects.all().order_by('id')
    serializer_class = NetworkSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('name','location')
    filterset_fields = ['name', 'location', 'owner']


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
#    permission_classes = [IsOwnerOrReadOnly]
    queryset = Lendable.objects.all().order_by('id')
    serializer_class = LendableSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('name',)
    filterset_fields = ['lendable_status', 'lendable_type', 'replacement_cost',
        'name', 'owner', 'location']

class LoanViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Loan.objects.all().order_by('id')
    serializer_class = LoanSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('lendable__owner','borrowing_user', 'lendable__name')
    filterset_fields = ['lendable','lendable__name', 'lendable__owner',
        'return_confirmed_by_borrower',
        'return_confirmed_by_lender',
        'lendable__owner',
        'borrowing_user',
        'confirmed_by_lender',
        'confirmed_by_borrower',
        ]


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
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('codename', 'name',)
    filterset_fields = ('codename', 'name')
    
class ContentTypeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = ContentType.objects.all().order_by('id')
    serializer_class = ContentTypeSerializer