from django.contrib import admin
from aboutme.models import AboutMe

class AboutMeAdmin(admin.ModelAdmin):
    fields = ('title', 'content')

admin.site.register(AboutMe, AboutMeAdmin)
