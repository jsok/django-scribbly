from django.contrib import admin

from pricing.models import ProductPriceCategory, CustomerPriceCategory, TaxCategory, DiscountMatrixEntry

class ProductPriceCategoryAdmin(admin.ModelAdmin):
    """
    """
    pass

class CustomerPriceCategoryAdmin(admin.ModelAdmin):
    """
    """
    pass

class TaxCategoryAdmin(admin.ModelAdmin):
    """
    """
    pass

class DiscountMatrixEntryAdmin(admin.ModelAdmin):
    """
    """
    model = DiscountMatrixEntry
    list_display = ('discount', 'customer_category', 'product_category')

    def matrix_view(self, request):
        from pricing.views import matrix
        from django.core.urlresolvers import reverse
        url = reverse('admin:pricing_discountmatrixentry_changelist', current_app="pricing")
        extra_context = {
                'opts': self.model._meta,
                'change': False,
                'is_popup': False,
                'save_as': True,
                'add': True,
                'has_delete_permission': False,
                'has_add_permission': True,
                'has_change_permission': True,
        }
        defaults = {
            'current_app': self.admin_site.name,
            'post_change_redirect': url,
            'extra_context': extra_context,
        }
        return matrix(request, **defaults)

    # Add custom matrix view to the admin model
    def get_urls(self):
        from django.conf.urls import patterns, url

        urls = patterns('',
                url(r'^matrix/$',
                    self.admin_site.admin_view(self.matrix_view),
                    name="pricing_discountmatrixentry_matrix")
                )
        urls += super(DiscountMatrixEntryAdmin, self).get_urls()
        return urls

admin.site.register(ProductPriceCategory, ProductPriceCategoryAdmin)
admin.site.register(CustomerPriceCategory, CustomerPriceCategoryAdmin)
admin.site.register(TaxCategory, TaxCategoryAdmin)
admin.site.register(DiscountMatrixEntry, DiscountMatrixEntryAdmin)
