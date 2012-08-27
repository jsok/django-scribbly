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

    try:
        quantity = int(request.POST.get("quantity"))
        if quantity < 0:
            raise ValueError
        quantity_error = False
    except:
        quantity = 0
        quantity_error = True

    # Render the new button to send back to client
    if quantity == 0 or quantity_error:
        button_t = loader.get_template("scribbly/catalog/add_button.html")
    else:
        button_t = loader.get_template("scribbly/catalog/order_button.html")
    button_c = RequestContext(request,
            {
                "product_pk": product.pk,
                "error": quantity_error,
            })

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

    # Render the updated cart icon to send back to client
    cart_items_count = len(request.session["cart_items"])
    cart_t = loader.get_template("scribbly/cart/cart_navbar.html")
    cart_c = RequestContext(request, { "cart_items_count": cart_items_count })

    result = simplejson.dumps({
        "product-id": product.pk,
        "product": product.name,
        "quantity": quantity if quantity > 0 else "",
        "button-div": button_t.render(button_c),
        "cart-nav-item": cart_t.render(cart_c),
    })

    return HttpResponse(result, content_type="application/json")
