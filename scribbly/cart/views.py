from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect, Http404

from product.models import Product

@login_required
def add_product_to_cart(request):
    if request.POST:
        print request.POST

        product_pk = request.POST.get("pk")
    else:
        product_pk = 4
    product = Product.objects.get(pk=product_pk)

    print product.name

    result = simplejson.dumps({
        "product": product.name,
    })

    return HttpResponse(result, content_type="application/json")

