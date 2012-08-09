from django.db import models

class Taxon(models.Model):
    """
    A taxonomy is applied to products and is used to categorise them.
    """
    name = models.CharField(max_length=50)
    path = models.TextField(blank=True)
    position = models.PositiveSmallIntegerField()

    # A taxon can be nested within another taxon
    parent = models.ForeignKey('self',
            related_name='children_set',
            null=True,
            blank=True)

    def save(self, *args, **kwargs):
        self.path = self.generate_path()
        super(Taxon, self).save(*args, **kwargs)

    def generate_path(self):
        return self.__unicode__()

    def __unicode__(self):
        path = ""
        parent = self.parent
        while parent != None:
            path = "/%s" % parent.name + path
            parent = parent.parent
        return path + "/" + self.name


    def get_children(self):
        return self.children_set.all()

    def get_products(self):
        return self.product_set.all()

    class Meta:
        verbose_name_plural = "Taxonomies"
