from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from photos.models import Gallery, Photo

class SpecialOrderingChangeList(ChangeList):
    def apply_special_ordering(self, queryset):
        order_type, order_by = [self.params.get(param, None) for param in ('ot', 'o')]
        special_ordering = self.model_admin.special_ordering
        if special_ordering and order_type and order_by:
            try:
                order_field = self.list_display[int(order_by)]
                ordering = special_ordering[order_field]
                if order_type == 'desc':
                    ordering = ['-' + field for field in ordering]
                queryset = queryset.order_by(*ordering)
            except IndexError:
                return queryset
            except KeyError:
                return queryset
        return queryset

    def get_query_set(self):
        queryset = super(SpecialOrderingChangeList, self).get_query_set()
        queryset = self.apply_special_ordering(queryset)
        return queryset

class GalleryAdmin(admin.ModelAdmin):
    fields = ('title', 'cover', 'is_public')
    list_display = ('title', 'created_date', 'is_public')
    ordering = ('title',)

class PhotoAdmin(admin.ModelAdmin):
    fields = ('gallery', 'image_source', 'caption', 'position', 'is_public')
    list_display = ('get_thumb', 'gallery', 'position', 'views', 'created_date', 'is_public')
    list_filter = ('gallery', 'is_public')
    special_ordering = {'gallery': ('gallery', 'is_public', 'position'), 'position': ('gallery', 'is_public', 'position')}
    
    def get_changelist(self, request, **kwargs):
        return SpecialOrderingChangeList

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo, PhotoAdmin)
