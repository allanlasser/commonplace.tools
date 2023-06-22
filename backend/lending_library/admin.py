from django.contrib import admin
from django.contrib.gis import admin as GISAdmin
from django.contrib.gis.db import models
from django import forms
from django.contrib.gis.geos import Point
from .models import Location, Network, LendableStatus, LendableType, Lendable, Loan, Photo

@admin.register(Location)
class LocationAdmin(GISAdmin.OSMGeoAdmin):
    pass

@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    pass

@admin.register(LendableStatus)
class LendableStatusAdmin(admin.ModelAdmin):
    pass
    
@admin.register(LendableType)
class LendableTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Lendable)
class LendableAdmin(admin.ModelAdmin):
    pass

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    pass

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass