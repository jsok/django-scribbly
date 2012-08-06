# django imports
from django.contrib import admin

# lfs imports
from customer.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(Customer, CustomerAdmin)
