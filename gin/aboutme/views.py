from django.shortcuts import render_to_response
from django.template import RequestContext
from aboutme.models import AboutMe

def index(request):
	info = AboutMe.objects.get(pk=1)
	return render_to_response('aboutme/index.html', { 'info': info }, context_instance=RequestContext(request))
