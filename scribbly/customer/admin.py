from django.contrib import admin

from customer.models import Customer, Company, Address

class AddressInlineAdmin(admin.StackedInline):
    model = Address
    extra = 0

class CompanyAdmin(admin.ModelAdmin):
    """
    """
    inlines = [AddressInlineAdmin]

class CustomerAdmin(admin.ModelAdmin):
    """
    """


admin.site.register(Company, CompanyAdmin)
admin.site.register(Customer, CustomerAdmin)
