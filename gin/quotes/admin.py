from django.contrib import admin
from quotes.models import Quote, Author, Tag

class QuoteAdmin(admin.ModelAdmin):
    #list_display = ('content', 'author')
    list_filter = ('author',)
    ordering = ('author__name',)

admin.site.register(Quote, QuoteAdmin)
admin.site.register(Author)
admin.site.register(Tag)
