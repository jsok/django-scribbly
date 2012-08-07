from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse

from core.context_processors import applist

from pricing.models import ProductPriceCategory, CustomerPriceCategory, DiscountMatrixEntry

def matrix(request,
        template_name='admin/pricing/discountmatrixentry/matrix.html',
        post_change_redirect=None,
        current_app=None, extra_context=None):

    if request.method == "POST":
        print request.POST.items()
        for key,val in request.POST.items():
            if key.startswith("discount"):
                print "Received new discount value: %s" % val
        return HttpResponseRedirect(post_change_redirect)

    product_cats = ProductPriceCategory.objects.all().order_by("name")
    customer_cats = CustomerPriceCategory.objects.all().order_by("name")

    discount_matrix = {}
    for p in product_cats:
        for c in customer_cats:
            discount_matrix[p.name] = {
                    c.name: None
                    }

    discounts = DiscountMatrixEntry.objects.all().order_by("id")
    for d in discounts:
        discount_matrix[d.product_category.name][d.customer_category.name] = d.discount

    context = {
        'app_list': applist(request),
        'app_label': "pricing",
        'matrix': discount_matrix,
        'matrix_columns': [c.name for c in customer_cats],
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)

