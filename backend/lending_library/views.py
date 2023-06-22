from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
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
#    permission_classes = [IsOwnerOrReadOnly]
    queryset = Lendable.objects.all().order_by('id')
    serializer_class = LendableSerializer

class LoanViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
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
    
class ContentTypeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = ContentType.objects.all().order_by('id')
    serializer_class = ContentTypeSerializer