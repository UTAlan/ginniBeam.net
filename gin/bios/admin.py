from django.contrib import admin
from bios.models import Category, Bio

class BioAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'relation', 'is_public')
    list_filter = ('category',)
    ordering = ('category', 'name')

admin.site.register(Category)
admin.site.register(Bio, BioAdmin)
