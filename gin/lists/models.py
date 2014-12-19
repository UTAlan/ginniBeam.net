from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=200)
    is_public = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
    
    def songcount(self):
        return Song.objects.filter(name=self).count()
    
    class Meta:
        ordering = ('name',)

class Artist(models.Model):
    name = models.CharField(max_length=200)
    is_public = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name

class Song(models.Model):
    name = models.ManyToManyField(Name)
    artist = models.ForeignKey(Artist)
    song_name = models.CharField(max_length=200)
    is_public = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.song_name
    
    def get_names(self):
        names = list(self.name.all())
        result = ''
        for n in names:
            result += n.name
            if n != names[-1]:
                result += ', '
        return result
