from django.test import TestCase
from faker import Faker
fake = Faker()
Faker.seed(0)

from lending_library.models import Location, Network
from django.contrib.gis.geos import Point
class LocationTestCase(TestCase):
    def setUp(self):
        pass 
        
    def test_location(self):
        loc = Location.objects.get()
        expected_object_name = loc.name
        self.assertEqual(str(loc), expected_object_name)


class NetworkTestCase(TestCase):
    def setUp(self):
        loc = Location.objects.get()
        Network.objects.create(name=faker.company(), location=loc)
    
    def test_network(self):
        network = Network.objects.get()
        expected_object_name = network.name
        self.assertEqual(str(network), expected_object_name)