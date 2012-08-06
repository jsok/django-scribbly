from django.contrib import admin

from pricing.models import ProductPriceCategory, CustomerPriceCategory, DiscountMatrixEntry

class ProductPriceCategoryAdmin(admin.ModelAdmin):
    """
    """
    pass

class CustomerPriceCategoryAdmin(admin.ModelAdmin):
    """
    """
    pass

class DiscountMatrixEntryAdmin(admin.ModelAdmin):
    """
    """
    pass

admin.site.register(ProductPriceCategory, ProductPriceCategoryAdmin)
admin.site.register(CustomerPriceCategory, CustomerPriceCategoryAdmin)
admin.site.register(DiscountMatrixEntry, DiscountMatrixEntryAdmin)
