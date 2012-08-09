from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from product.models import Product

from taxon.models import Taxon
from taxon.utils import get_taxon_map, get_root_taxons

def index(request, taxon=None, template_name="scribbly/catalog/index.html"):
    taxon_map = get_root_taxons()

    # A taxon map should exist, will only happen if none have been created
    if taxon_map is []:
        raise Http404

    # We will display the first root taxon by default if none specified
    if taxon is None:
        selected_taxon = taxon_map[0]
    else:
        try:
            selected_taxon = Taxon.objects.get(name__iexact=taxon)
        except Taxon.DoesNotExist:
            return HttpResponseRedirect(
                    reverse('catalog.views.index'))

    context = {
            "selected_taxon": selected_taxon,
            "taxon_map": taxon_map,
    }

    return render_to_response(template_name,
            RequestContext(request, context))

