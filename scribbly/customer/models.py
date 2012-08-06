from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    """
    A customer is the glue which binds a Django user and a Company model
    together.
    """
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return "%s" % self.user.email
