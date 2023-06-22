from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from lending_library.models import Location, Network, LendableStatus, LendableType, Lendable, Loan, UserProfile 
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
#        fields = ['first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined']
        fields = '__all__'

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
     #   exclude = ('contenttype',)

class ContentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'

class LendableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lendable
        fields = '__all__'

class LendableTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LendableType
        fields = '__all__'

class LendableStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LendableStatus
        fields = '__all__'

class NetworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'

class LoanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

