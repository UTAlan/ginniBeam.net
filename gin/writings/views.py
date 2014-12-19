from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from writings.models import Category, Entry
import urllib

def index(request):
    categories = Category.objects.all()
    
    writings = []
    for cat in categories:
        year = Entry.objects.filter(is_public=True).filter(category=cat.id).values('year').distinct().order_by('-year')
        
        years = []
        for y in year:
            if request.user.is_authenticated():
                entries = Entry.objects.filter(is_public=True).filter(Q(groups__in=request.user.groups.all()) | Q(groups__isnull=True)).filter(category=cat.id).filter(year=y['year']).order_by('title')
            else:
                entries = Entry.objects.filter(is_public=True).filter(groups__isnull=True).filter(category=cat.id).filter(year=y['year']).order_by('title')
            years.append([y['year'], entries])
        
        writings.append([cat, years])                    
    
    return render_to_response('writings/index.html', {'writings': writings, 'categories': categories}, context_instance=RequestContext(request))

def entry(request, title):
    title = urllib.unquote(urllib.unquote(title.encode('ASCII','ignore')))
    entry = Entry.objects.filter(is_public=True).filter(title=title).values('content')
    
    return render_to_response('writings/entry.html', { 'title': title, 'content': entry[0]['content'] }, context_instance=RequestContext(request))
