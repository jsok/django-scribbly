from django.contrib import admin

from taxon.models import Taxon

class TaxonAdmin(admin.ModelAdmin):
    model = Taxon
    list_display = ('path', 'position', 'name')
    list_editable = ['position', 'name']

    readonly_fields = ('path',)

    fieldsets = (
        (None, {
            'fields': ('path', 'name', 'position')
        }),
    )

admin.site.register(Taxon, TaxonAdmin)
