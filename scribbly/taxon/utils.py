from taxon.models import Taxon

def get_root_taxons():
    return Taxon.objects.filter(parent__isnull=True).order_by('position')

