from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name

class Quote(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Author)
    tag = models.ForeignKey(Tag)
    
    def __unicode__(self):
        return self.author.name + ' - ' + self.content
