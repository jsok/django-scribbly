from django.contrib import admin

from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('sku', 'name', 'price')
    list_filter = ('taxons__path',)
    filter_horizontal = ('taxons',)
    search_fields = ('sku', 'name')

    fieldsets = (
        ('Product', {
            'fields': ('sku', 'name', 'price')
        }),
        ('Taxonomies', {
            'fields': ('taxons',)
        }),
    )

admin.site.register(Product, ProductAdmin)
