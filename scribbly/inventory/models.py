from django.db import models

from product.models import Product

class InventoryItem(models.Model):
    """
    An inventory item has a one-to-one correspondence with a Product
    in order to track its inventory movements.

    Things tracked:
    - Current stock on hand
    - All orders which contain this product
    - All backorders (pending and fulfilled) for this product


    """
    product = models.OneToOneField(Product,
            primary_key=True,
            related_name='inventory_item')

    on_hand = models.PositiveIntegerField()

    def __unicode__(self):
        return self.product.name

    class Meta:
        verbose_name = "Inventory Item"
        verbose_name_plural = "Inventory"

    @property
    def on_hand_fuzzy(self):
        """Return fuzzy quantity."""
        if self.on_hand <= 5:
            return self.on_hand
        elif self.on_hand <= 10:
            return "5-10"
        elif self.on_hand <= 20:
            return "11-20"
        else:
            return "20+"

