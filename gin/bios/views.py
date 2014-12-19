from django.shortcuts import render_to_response
from django.template import RequestContext
from bios.models import Category, Bio
import urllib

def index(request):
    categories = Category.objects.all()
    
    bios = []
    for cat in categories:
        bios.append(Bio.objects.filter(category=cat.id).order_by('name'))
    
    return render_to_response('bios/index.html', { 'bios':bios, 'categories':categories }, context_instance=RequestContext(request))

def detail(request, bio_name):
    bio_name = urllib.unquote(urllib.unquote(bio_name.encode('ASCII','ignore')))
    bio = Bio.objects.get(name=bio_name)
    
    return render_to_response('bios/detail.html', { 'bio': bio }, context_instance=RequestContext(request))
