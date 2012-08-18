from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from customer.utils import get_current_customer
from pricing.utils import get_products_for_taxon
from taxon.models import Taxon
from taxon.utils import get_root_taxons

@login_required
def index(request, taxon_slug=None, template_name="scribbly/catalog/index.html"):
    taxon_map = get_root_taxons()

    # A taxon map should exist, will only happen if none have been created
    if taxon_map is []:
        raise Http404

    # We will display the first root taxon by default if none specified
    if taxon_slug is None:
        selected_taxon = taxon_map[0]
    else:
        try:
            selected_taxon = Taxon.objects.get(slug=taxon_slug)
        except Taxon.DoesNotExist:
            return HttpResponseRedirect(
                    reverse('catalog.views.index'))

    customer = get_current_customer(request)
    priced_products = get_products_for_taxon(selected_taxon, customer)

    # Update quantities in priced_products from the cart_items
    if request.session.has_key("cart_items"):
        cart_items = request.session["cart_items"]

        for product_pk, pp in priced_products.iteritems():
            if cart_items.has_key(product_pk):
                pp.quantity = cart_items[product_pk]

    context = {
            "selected_taxon": selected_taxon,
            "taxon_map": taxon_map,
            "priced_products": priced_products,
    }

    return render_to_response(template_name,
            RequestContext(request, context))
