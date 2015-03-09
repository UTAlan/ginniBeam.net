from lists.models import Name, Artist, Song
from django.contrib import admin

class NameAdmin(admin.ModelAdmin):
    list_display = ('name', 'songcount', 'is_public')
    ordering = ('name',)
    search_fields = ['name']
    
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_public')
    ordering = ('name','is_public')
    search_fields = ['name']
    
class SongAdmin(admin.ModelAdmin):
    list_display = ('song_name', 'artist', 'get_names', 'is_public')
    list_filter = ('is_public',)
    ordering = ('is_public', 'song_name')
    search_fields = ['song_name','artist__name',]
    filter_horizontal = ('name',)
    #raw_id_fields = ('artist',)

admin.site.register(Name, NameAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song, SongAdmin)
