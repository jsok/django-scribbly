from django.conf.urls.defaults import *

# Tastypie API for Product models
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.utils import trailing_slash

from product.models import Product

class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
        exclude = ['price_category', 'taxons']
        allowed_methods = ['get']
        serializer = Serializer(formats=['json',])

    def override_urls(self):
        return [
            url(
                r"^(?P<resource_name>%s)/search%s$" % (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_search'),
                name="api_get_search"),
        ]

    def get_search(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.throttle_check(request)

        ## Do the query.
        term = request.GET.get('q', '')
        object_list = Product.objects.filter(name__contains=term)

        objects = []

        for result in object_list:
            bundle = self.build_bundle(obj=result, request=request)
            bundle = self.full_dehydrate(bundle)
            objects.append(bundle)

        object_list = {
            'objects': objects,
        }

        self.log_throttled_access(request)
        return self.create_response(request, object_list)
