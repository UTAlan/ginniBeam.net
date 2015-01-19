import os, sys
sys.path.append(os.environ['HOME'] + '/lib/python')

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from gdata.photos import service

def index(request):
    info = {}
    
    gd_client = service.PhotosService()
    gd_client.email = settings.GOOGLE_EMAIL
    gd_client.password = settings.GOOGLE_PASS
    gd_client.source = settings.SITE_NAME
    gd_client.ProgrammaticLogin()
    
    google_albums = gd_client.GetUserFeed()
    albums = []
    titles = []
    for google_album in google_albums.entry:
      if google_album.rights.text == 'public':
        a = {}
        a['title'] = google_album.title.text
        a['thumb'] = google_album.media.thumbnail[0].url
        a['id'] = google_album.gphoto_id.text
        albums.append(a)
        titles.append(google_album.title.text)

    titles.sort(reverse=True)
    
    info['albums'] = []
    for t in titles:
      for a in albums:
        if a['title'] == t:
          info['albums'].append(a)
          continue
    
    return render_to_response('pics/index.html', { 'info': info }, context_instance=RequestContext(request))

def album(request, album_id):
    info = {}
    
    gd_client = service.PhotosService()
    gd_client.email = settings.GOOGLE_EMAIL
    gd_client.password = settings.GOOGLE_PASS
    gd_client.source = settings.SITE_NAME
    gd_client.ProgrammaticLogin()
    
    album = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s' % (settings.GOOGLE_USER, album_id))
    info['album'] = {}
    info['album']['title'] = album.title.text
    info['album']['id'] = album_id
    
    photos = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo' % (settings.GOOGLE_USER, album_id))
    
    info['photos'] = []
    for photo in photos.entry:
      p = {}
      p['caption'] = photo.media.description.text
      p['thumb'] = photo.media.thumbnail[0].url
      p['img'] = photo.content.src
      p['id'] = photo.gphoto_id.text
      info['photos'].append(p)
    
    return render_to_response('pics/album.html', { 'info': info }, context_instance=RequestContext(request))
