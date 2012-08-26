from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.template import RequestContext, loader
from django.utils import simplejson

from product.models import Product

@login_required
def add_product_to_cart(request):
    """
    AJAX request to add the POST'ed product to the cart.

    POST format:
    {
      "product-id": id,
      "quantity": qty,
    }

    Logic:
    Quantity  > 0 -> add/update product in cart
    Quantity == 0 or None -> remove from cart

    Errors:
    Return 404 if bad product ID supplied.
    """

    product = get_object_or_404(Product, pk=request.POST.get("product-id"))

    quantity_error = False
    quantity = request.POST.get("quantity")
    if not quantity:
        quantity = 0
    elif int(quantity) < 0:
        quantity_error = True
    else:
        quantity = int(quantity)

    # Render the result to send back to client
    if quantity == 0 or quantity_error:
        t = loader.get_template("scribbly/catalog/add_button.html")
    else:
        t = loader.get_template("scribbly/catalog/order_button.html")
    c = RequestContext(request,
            {
                "product_pk": product.pk,
                "error": quantity_error,
            })

    result = simplejson.dumps({
        "product-id": product.pk,
        "product": product.name,
        "quantity": quantity if quantity > 0 else "",
        "button-div": t.render(c),
    })

    print quantity_error, quantity

    if not quantity_error:
        # Add product to session cart
        if request.session.get("cart_items") is None:
            request.session["cart_items"] = {}

        cart_items = request.session["cart_items"]
        if cart_items.has_key(product.pk):
            if (quantity == 0):
                del cart_items[product.pk]
            else:
                cart_items[product.pk] = quantity
        else:
            cart_items[product.pk] = quantity
        request.session.modified = True

    return HttpResponse(result, content_type="application/json")
