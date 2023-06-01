from django.contrib import admin
from .models import Location, Network, LendableStatus, LendableType, Lendable, Loan

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
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

