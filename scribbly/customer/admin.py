from django.contrib import admin

from customer.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(Customer, CustomerAdmin)
