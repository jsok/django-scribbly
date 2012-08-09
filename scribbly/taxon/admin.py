from django.contrib import admin

from taxon.models import Taxon

class TaxonAdmin(admin.ModelAdmin):
    model = Taxon
    list_display = ('path', 'position', 'name')
    list_editable = ['position', 'name']
    prepopulated_fields = {"slug": ("name",)}

    readonly_fields = ('path',)

    fieldsets = (
        (None, {
            'fields': ('path', 'name', 'slug', 'position', 'parent')
        }),
    )

admin.site.register(Taxon, TaxonAdmin)
