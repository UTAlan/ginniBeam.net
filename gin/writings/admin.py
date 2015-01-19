from writings.models import Category, Entry
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'year', 'description', 'is_public')
    list_filter = ('year', 'category')
    ordering = ('category', 'year', 'title')

admin.site.register(Category)
admin.site.register(Entry, EntryAdmin)


