from django.contrib import admin

from product.models import Product
from inventory.models import InventoryItem

class ProductInventoryAdmin(admin.TabularInline):
    model = InventoryItem
    def has_delete_permission(self, request, obj=None):
        return False

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
    inlines = [ProductInventoryAdmin]

admin.site.register(Product, ProductAdmin)
