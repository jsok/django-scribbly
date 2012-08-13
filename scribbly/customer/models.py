from django.contrib.auth.models import User
from django.db import models

from pricing.models import CustomerPriceCategory

class Company(models.Model):
    """
    Details of a company (can be either a customer or supplier).
    """
    name = models.CharField(max_length=100, blank=False)

    abn = models.CharField(max_length=100, blank=True)
    acn = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"

class Supplier(models.Model):
    """
    A supplier of products the warehouse strocks.
    Able to submit purchase orders and receive inventory from them.
    """
    name = models.CharField(max_length=100, blank=False)

    # TODO: Link to a Company

class Customer(models.Model):
    """
    A customer is the glue which binds a Django user and a Company model
    together.
    """
    user = models.ForeignKey(User, blank=True, null=True)
    company = models.OneToOneField(Company, related_name='company')

    # Pricing related
    customer_category = models.ForeignKey(CustomerPriceCategory, null=False)

    def __unicode__(self):
        return "[%s] %s" % (self.company.name, self.user.email)

class Address(models.Model):
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    company = models.ForeignKey(Company)

    ADDRESS_TYPES = (
            ('BILLING', "Billing"),
            ('SHIPPING', "Shipping"),
    )
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPES)

    def __unicode__(self):
        if self.address_line_2:
            address = self.address_line_1 + ", " + self.address_line_2
        else:
            address = self.address_line_1
        return "%s / %s %s " % (
                address,
                self.city,
                self.postcode)
