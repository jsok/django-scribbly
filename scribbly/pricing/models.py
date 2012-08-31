from django.db import models

class ProductPriceCategory(models.Model):
    """
    A Price Category for products which tells categorises
    similar products that have the same discounting model.
    """
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product Price Categories"

class CustomerPriceCategory(models.Model):
    """
    A Customer Category which allocates a discounting
    structure to a customer.
    """
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Customer Price Categories"

class DiscountMatrixEntry(models.Model):
    """
    An entry in the discount matrix which matches
    ProductPriceCategories with CustomerPriceCategories
    and gives the resulting discount.
    """
    discount = models.FloatField(default=0.0)

    product_category = models.ForeignKey(ProductPriceCategory)
    customer_category = models.ForeignKey(CustomerPriceCategory)

    def __unicode__(self):
        return "%g" % self.discount

    class Meta:
        verbose_name_plural = "Discount Matrix Entries"

class TaxCategory(models.Model):
    name = models.CharField(max_length=10)
    rate = models.FloatField("Tax Rate", default = 0.0)

    def __unicode__(self):
        return "%s (%d%%)" % (self.name, self.rate)

    class Meta:
        verbose_name_plural = "Tax Categories"

