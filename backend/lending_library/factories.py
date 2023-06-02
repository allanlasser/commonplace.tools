import factory
from . import models

class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Location

    name = factory.Faker('first_name')
    address1 = factory.Faker()
    address2 = factory.Faker()
    city = factory.Faker()
    state = factory.Faker()
    postal_code = factory.Faker()
    country = factory.Faker('country_code')
    cords = factory.Faker('location_on_land') #(coords_only=True)
    point_geometry = Point(float(cords[0]), float(cords[1]))



class NetworkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Network

    location = factory.SubFactory(LocationFactory)
    name = factory.Faker('company')

class LendableStatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.LendableStatus


class LendableTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.LendableType


class LendableFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Lendable


class LoanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Loan

class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.UserProfile


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Photo