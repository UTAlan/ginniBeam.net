from django.contrib import admin
from blog.models import Category, Tag, Post, Comment

class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'category', 'tags', 'groups', 'is_public')
    list_display = ('title', 'category', 'created_date', 'is_public')
    list_filter = ('category', 'groups', 'is_public')
    ordering = ('-created_date',)
    
    class Media:
        js = ("http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js","http://www.zurb.com/javascripts/plugins/jquery.textchange.min.js",)

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
