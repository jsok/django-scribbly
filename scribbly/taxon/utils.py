from taxon.models import Taxon

def get_root_taxons():
    return Taxon.objects.filter(parent__isnull=True).order_by('position')

def get_taxon_map():
    taxon_map = []
    roots = get_root_taxons()

    for taxon in roots:
        child_map = map_for_taxon(taxon)
        taxon_map.append((taxon, child_map))

    return taxon_map

def map_for_taxon(taxon):
    child_map = []
    for c in taxon.children_set.all():
        child_map.append((c, map_for_taxon(c)))
    return child_map

