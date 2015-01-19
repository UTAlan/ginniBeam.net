from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.title

class Bio(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=200)
#    picture = models.FileField(upload_to='bios/', blank=True, null=True)
    pic = models.ImageField(upload_to='bios', blank=True, null=True)
    birthdate = models.CharField(max_length=200, blank=True, null=True)
    relation = models.CharField(max_length=200, blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'bios'
