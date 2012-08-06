from django.db import models

class Product(models.Model):
    """
    A product in the inventory which can be sold.
    """
    sku = models.CharField("SKU", max_length=50)
    name = models.CharField(max_length=100)

    # Inventory tracking
    # on_hand = models.IntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)
    # price_category = models.ForeignKey(ProductPriceCategory)

    def __unicode__(self):
        return self.name
