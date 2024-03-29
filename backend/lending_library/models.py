from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import requests

class Location(models.Model):
    """
    Location contains a street address and a point and can be used for people, things, networks, etc
    """
    name = models.CharField("Address name", max_length=1024,blank=True)
    address1 = models.CharField("Address line 1", max_length=1024, blank=True)
    address2 = models.CharField("Address line 2", max_length=1024, blank=True)
    city = models.CharField("City or Town", max_length=1024, blank=True)
    state = models.CharField("State", max_length=2, blank=True)
    postal_code = models.CharField("Zip or Postal Code", max_length=12)
    country = models.CharField("Country", max_length=2, blank=True)
    point_geometry = models.PointField("Location Point", srid=4326, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        """
        Geocode US based address using the US Census Geocoder tool. 
        Only works with US addresses, we would need to use a different service, 
        perhaps Smarty or Google paid APIs, to geocode non-US addresses.
        """
        recode = False
        
        # Check to see if we are new, or modifying any of the specific fields that matter, and trigger re-geocoding.
        if self.pk is not None:
            orig = Location.objects.get(pk=self.pk)
            fields_to_check = ('address1', 'city', 'state', 'postal_code', 'country')
            for field in fields_to_check:
                if getattr(orig, field) != getattr(self, field):
                    recode = True
                    break
        if self.country == 'US' and (recode == True or self.point_geometry is None):
            try:
                URLbase = 'https://geocoding.geo.census.gov/geocoder/locations/address?format=json&benchmark=Public_AR_Current&'
                URLparam = f'street={self.address1}&city={self.city}&state={self.state}&zip={self.postal_code}'
                r = requests.get(URLbase+URLparam)
                r.raise_for_status()
                r_dict = r.json()
                print(r_dict)
                lon = r_dict['result']['addressMatches'][0]['coordinates']['x']
                lat = r_dict['result']['addressMatches'][0]['coordinates']['y']
                self.point_geometry = Point(lon, lat, srid='4326')
            except Exception as e:
                print('Geocoding request error: {}'.format(e,))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Network(models.Model):
    """
    A lending network brings people together. Typically visablility is limited to within one network.
    """
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name} - {self.location}"


class LendableStatus(models.Model):
    """
    Different possible statues - Available, Broken, Missing, On-Loan
    These are defined on a per-network basis to allow localization and customization.
    """
    name = models.CharField("Status of Lendable", max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    network = models.ForeignKey(Network, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Lendable Statuses"


    def __str__(self):
        return self.name

class LendableType(models.Model):
    """
    Different possible types of lendable objects - books, tools, clothes, etc
    These are defined on a per-network basis to allow localization and customization.
    """
    name = models.CharField("Type of Lendable", max_length=1024)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    network = models.ForeignKey(Network, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lendable(models.Model):
    lendable_status = models.ForeignKey(LendableStatus, on_delete=models.CASCADE)
    lendable_type = models.ForeignKey(LendableType, on_delete=models.CASCADE)
    replacement_cost = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=1024,)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    location_updated = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

class Loan(models.Model):
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    lendable = models.ForeignKey(Lendable, on_delete=models.CASCADE, blank=False)

    @property
    def lending_user(self):
        return self.lendable.owner

    @property
    def lending_network(self):
        return self.lendable.owner.profile.network

    # The lender and the borrower both have to confirm the
    # loan or it lives in purgetory/a confirmation queue before
    # eventually being nullified/deleted.
    confirmed_by_lender = models.BooleanField(default=False)

    borrowing_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    confirmed_by_borrower = models.BooleanField(default=False)

    returned_datetime = models.DateTimeField(null=True)
    return_confirmed_by_borrower = models.BooleanField(default=False)
    return_confirmed_by_lender = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.lendable} - {self.lending_user} to {self.borrowing_user} "


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    network = models.ForeignKey(Network, on_delete=models.CASCADE,)
    phone_number = models.CharField(max_length=12, blank=True)
    url = models.URLField("Website", blank=True)
    bio = models.TextField(blank=True)
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.SET_NULL)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user} - {self.network} - {self.bio:.20}"


class Photo(models.Model):
    # So I made this a generic relation because we can have photos of
    # different things, both lendables, users, etc
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    image = models.ImageField(
        upload_to="uploads/%Y/%m/%d/",
        blank=False,
        null=False,
        height_field='height',
        width_field='width'
    )
    height = models.PositiveIntegerField(null=True, blank=True)
    width = models.PositiveIntegerField(null=True, blank=True)
    caption = models.CharField(max_length=1024, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.name
