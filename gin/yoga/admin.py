from django.contrib import admin
from yoga.models import Yoga

class YogaAdmin(admin.ModelAdmin):
    fields = ('title', 'content')

admin.site.register(Yoga, YogaAdmin)
