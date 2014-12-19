from django.db import models, transaction
from django.contrib.auth.models import User, Group
from photos.fields import PositionField
from stdimage import StdImageField

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover = models.ForeignKey("Photo", null=True, blank=True, related_name='cover')
    groups = models.ManyToManyField(Group, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ('is_public', 'title')

class Photo(models.Model):
    gallery = models.ForeignKey(Gallery)
    image_source = StdImageField(upload_to='photos/', size=(640, 480), thumbnail_size=(225, 150))
    caption = models.TextField(blank=True, null=True)
    position = PositionField(unique_for_field='gallery')
    groups = models.ManyToManyField(Group, blank=True)
    views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    
    save = transaction.commit_on_success(models.Model.save)
    
    def __unicode__(self):
        return self.gallery.title + ' ' + str(self.position)
    
    def get_thumb(self):
        return '<img src="/media/%s" height="150px" />' % self.image_source
    
    def get_full(self):
        return '<img src="/media/%s" />' % self.image_source
    
    get_thumb.allow_tags = True
    get_full.allow_tags = True

class Comment(models.Model):
    photo = models.ForeignKey(Photo)
    author = models.ForeignKey(User, blank=True, null=True, related_name='PhotoComment')
    author_name = models.CharField(max_length=200, null=True)
    author_email = models.EmailField(null=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    
    def __unicode__(self):
        result = ''
        if self.author:
            result = self.author.username
        else:
            result = self.author_name
        return result + ': ' + self.content
