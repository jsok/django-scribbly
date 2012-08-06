from django.shortcuts import render_to_response
from django.template import RequestContext

from product.models import Product

def products(request, template_name="scribbly/product/index.html"):
    products = Product.objects.all().order_by('name')

    return render_to_response(template_name,
            RequestContext(request, {
                "products": products,
                }))
