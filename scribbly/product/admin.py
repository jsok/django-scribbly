from django.contrib import admin

from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('sku', 'name', 'price')
    list_filter = ('taxons__path',)
    filter_horizontal = ('taxons',)
    search_fields = ('sku', 'name')
    prepopulated_fields = {"slug": ("name",)}

    fieldsets = (
        ('Product', {
            'fields': ('sku', 'name', 'slug',)
        }),
        ('Pricing', {
            'fields': ('price', 'price_category',)
        }),
        ('Taxonomies', {
            'fields': ('taxons',)
        }),
    )

admin.site.register(Product, ProductAdmin)
