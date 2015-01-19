from django.shortcuts import render_to_response
from django.template import RequestContext
from lists.models import Name, Artist, Song
import urllib

def index(request):
    return render_to_response('lists/index.html', {  }, context_instance=RequestContext(request))

def namesongs(request):
    return render_to_response('lists/namesongs/index.html', { }, context_instance=RequestContext(request))

def list_names(request, name):
    name_list = Name.objects.filter(name__startswith=name).order_by('name')
    return render_to_response('lists/namesongs/list_names.html', { 'name': name, 'name_list': name_list }, context_instance=RequestContext(request))

def list_artists(request, artist):
    if artist.isdigit():
        artist_list = Artist.objects.filter(name__regex=r'^([0-9])').order_by('name')
    else:
        artist_list = Artist.objects.filter(name__startswith=artist).order_by('name')
    return render_to_response('lists/namesongs/list_artists.html', { 'artist': artist, 'artist_list': artist_list }, context_instance=RequestContext(request))

def display_name(request, name):
    name = urllib.unquote(urllib.unquote(name.encode('ASCII','ignore')))
    n = Name.objects.get(name=name)
    song_list = Song.objects.filter(name=n).order_by('song_name')
    return render_to_response('lists/namesongs/display_name.html', { 'title': name, 'song_list': song_list }, context_instance=RequestContext(request))

def display_artist(request, artist):
    artist = urllib.unquote(urllib.unquote(artist.encode('ASCII','ignore')))
    a = Artist.objects.get(name=artist)
    song_list = Song.objects.filter(artist=a).order_by('song_name')
    
    is_digit = False
    if artist[0].isdigit():
        is_digit = True
    
    return render_to_response('lists/namesongs/display_artist.html', { 'title': artist, 'song_list': song_list, 'is_digit': is_digit }, context_instance=RequestContext(request))
