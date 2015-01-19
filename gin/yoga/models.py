from django.db import models

class Yoga(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	
	def __unicode__(self):
		return self.title
