from django.shortcuts import render_to_response
from django.template import RequestContext
from yoga.models import Yoga

def index(request):
	info = Yoga.objects.get(pk=1)
	return render_to_response('yoga/index.html', { 'info': info }, context_instance=RequestContext(request))
