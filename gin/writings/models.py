from django.db import models
from django.contrib.auth.models import Group

class Category(models.Model):
    title = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.title

class Entry(models.Model):
    category = models.ForeignKey(Category)
    groups = models.ManyToManyField(Group, blank=True)
    title = models.CharField(max_length=200)
    year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    content = models.TextField()
    is_public = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.title
