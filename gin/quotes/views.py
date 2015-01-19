from django.shortcuts import render_to_response
from django.template import RequestContext
from quotes.models import Quote, Author, Tag

def index(request):
    info = {}
    
    info['quotes'] = Quote.objects.all().order_by('author__name')
    
    return render_to_response('quotes/index.html', { 'info': info }, context_instance=RequestContext(request))
