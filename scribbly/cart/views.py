from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.template import RequestContext, loader
from django.utils import simplejson

from product.models import Product

@login_required
def add_product_to_cart(request):
    product = get_object_or_404(Product, pk=request.POST.get("product-id"))

    quantity = request.POST.get("quantity")
    if not quantity or int(quantity) == 0:
        return HttpResponseBadRequest("Please enter a quantity")
    quantity = int(quantity)

    # Render the partial for the update button
    t = loader.get_template("scribbly/catalog/order_button.html")
    c = RequestContext(request, {"product_pk": product.pk})

    result = simplejson.dumps({
        "product-id": product.pk,
        "product": product.name,
        "quantity": quantity,
        "button-div": t.render(c),
    })

    # Add product to session cart
    if request.session.get("cart_items") is None:
        request.session["cart_items"] = {}

    cart_items = request.session["cart_items"]
    if cart_items.has_key(product.pk):
        cart_items[product.pk] += quantity
    else:
        cart_items[product.pk] = quantity
    request.session.modified = True

    return HttpResponse(result, content_type="application/json")
