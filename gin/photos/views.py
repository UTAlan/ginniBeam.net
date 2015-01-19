from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from photos.models import Gallery, Photo, Comment
from photos.forms import CommentForm
from recaptcha.client import captcha

def index(request, page_id=1):
    info = {}
    per_page = 10
    
    if request.user.is_authenticated():
        galleries = Gallery.objects.filter(is_public=True).filter(Q(groups__in=request.user.groups.all()) | Q(groups__isnull=True)).order_by('-title')
    else:
        galleries = Gallery.objects.filter(is_public=True).filter(groups__isnull=True).order_by('-title')
    
    for g in galleries:
        if g.cover is None:
            cover = Photo.objects.filter(is_public=True).filter(gallery=g)
            if cover.count() > 0:
                g.cover = cover[0]
    
    paginator = Paginator(galleries, per_page)
    
    try:
      page = int(page_id)
    except ValueError:
      page = 1
    
    try:
      info['galleries'] = paginator.page(page)
    except (EmptyPage, InvalidPage):
      info['galleries'] = paginator.page(paginator.num_pages)
    
    return render_to_response('photos/index.html', { 'info': info }, context_instance=RequestContext(request))

def gallery(request, gallery_name, page_id=1):
    info = {}
    per_page = 10
    
    info['gallery'] = Gallery.objects.get(title=gallery_name)
    photos = Photo.objects.filter(is_public=True).filter(gallery=info['gallery']).order_by('position').order_by('created_date')
    paginator = Paginator(photos, per_page)
    
    try:
      page = int(page_id)
    except ValueError:
      page = 1
    
    try:
      info['photos'] = paginator.page(page)
    except (EmptyPage, InvalidPage):
      info['photos'] = paginator.page(paginator.num_pages)
    
    return render_to_response('photos/gallery.html', { 'info': info }, context_instance=RequestContext(request))

def photo(request, gallery_name, photo_id):
    info = {}
    per_page = 1
    
    info['gallery'] = Gallery.objects.get(title=gallery_name)
    info['photo'] = Photo.objects.get(pk=photo_id)
    info['comment_list'] = Comment.objects.filter(photo=info['photo'])
    info['form'] = CommentForm()
    
    photos = Photo.objects.filter(is_public=True).filter(gallery=info['gallery']).order_by('position').order_by('created_date')
    paginator = Paginator(photos, per_page)
    
    try:
      page = int(info['photo'].position + 1)
    except ValueError:
      page = 1
    
    try:
      info['photos'] = paginator.page(page)
    except (EmptyPage, InvalidPage):
      info['photos'] = paginator.page(paginator.num_pages)
    
    if info['photos'].has_previous():
      info['prev_photo'] = Photo.objects.filter(gallery=info['gallery']).filter(position=info['photo'].position - 1)[0]
    if info['photos'].has_next():
      info['next_photo'] = Photo.objects.filter(gallery=info['gallery']).filter(position=info['photo'].position + 1)[0]
    
    for c in info['comment_list']:
        if c.author_id:
            u = User.objects.get(pk=c.author_id)
            c.author_name = u.username
            c.author_email = u.email
    
    return render_to_response('photos/photo.html', { 'info': info }, context_instance=RequestContext(request))

def comment(request, gallery_name, photo_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if not request.user.is_authenticated():
                r = captcha.submit(request.POST['recaptcha_challenge_field'], request.POST['recaptcha_response_field'], settings.RECAPTCHA_PRIVATE_KEY, request.META['REMOTE_ADDR'])
                if not r.is_valid:
                    return redirect('/photos/'+gallery_name+'/'+photo_id+'/') # Invalid form entry
            f = form.save(commit=False);
          
            f.photo_id = photo_id
            if request.user.is_authenticated():
                f.author_id = request.user.id
                f.author_name = ''
                f.author_email = ''
            f.save()
        
            email_msg  = 'You have a new comment at http://www.alanbeam.net/photos/'+gallery_name+'/'+photo_id+'/#comments'
            email_from = 'no-reply@alanbeam.net'
            email_to   = ['vtbeam@gmail.com', 'alan@alanbeam.net']
        
            # Send email notification
            EmailMessage('New Photo Comment - AlanBeam.net', email_msg, email_from, email_to)
        
            return redirect('/photos/'+gallery_name+'/'+photo_id+'/#comments') # Go back to blog with new comment
        else:
            return redirect('/photos/'+gallery_name+'/'+photo_id+'/') # Invalid form entry
    else:
        return redirect('/photos/'+gallery_name+'/'+photo_id+'/') # Go back to blog
