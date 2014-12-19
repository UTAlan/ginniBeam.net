from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.db.models import Q
from blog.models import Category, Tag, Post, Comment
from blog.forms import CommentForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
import math
import smtplib
from recaptcha.client import captcha
from django.contrib.sites.models import Site
from akismet import Akismet

def index(request, page_id=1):
    page_id = int(page_id)
    start_index = 5 * (page_id - 1)
    end_index = start_index + 5
    
    if request.user.is_authenticated():
      all_posts = Post.objects.filter(is_public=True).filter(Q(groups__in=request.user.groups.all()) | Q(groups__isnull=True)).order_by('-created_date')
    else:
      all_posts = Post.objects.filter(is_public=True).filter(groups__isnull=True).order_by('-created_date')
    
    recent_posts = all_posts[start_index:end_index]
    num_pages = math.ceil(all_posts.count() / 5.0)
    
    display_page_nav = True
    if page_id == 1:
        if page_id == num_pages:
            display_page_nav = False
    
    # If invalid page number, redirect to home page
    #if recent_posts.count() == 0:
      #return redirect('/')
    
    for post in recent_posts:
      post.comment_list = Comment.objects.filter(post=post).filter(is_public=True)
    
    return render_to_response('blog/list.html', { 'recent_posts': recent_posts, 'page_id': page_id, 'num_pages': num_pages, 'display_page_nav': display_page_nav }, context_instance=RequestContext(request))

def category(request, cat_name, page_id=1):
    page_id = int(page_id)
    start_index = 5 * (page_id - 1)
    end_index = start_index + 5
    
    cat = Category.objects.get(title=cat_name)
    
    if request.user.is_authenticated():
      all_posts = Post.objects.filter(is_public=True).filter(Q(groups__in=request.user.groups.all()) | Q(groups__isnull=True)).filter(category=cat).order_by('-created_date')
    else:
      all_posts = Post.objects.filter(is_public=True).filter(groups__isnull=True).filter(category=cat).order_by('-created_date')
    
    recent_posts = all_posts[start_index:end_index]
    num_pages = math.ceil(all_posts.count() / 5.0)
    
    display_page_nav = True
    if page_id == 1:
        if page_id == num_pages:
            display_page_nav = False
    
    # If invalid page number, redirect to home page
    if recent_posts.count() == 0:
      return redirect('/')
  
    for post in recent_posts:
      post.comment_list = Comment.objects.filter(post=post).filter(is_public=True)
    
    return render_to_response('blog/list.html', { 'recent_posts': recent_posts, 'page_id': page_id, 'num_pages': num_pages, 'display_page_nav': display_page_nav }, context_instance=RequestContext(request))

def tag(request, tag_name, page_id=1):
    page_id = int(page_id)
    start_index = 5 * (page_id - 1)
    end_index = start_index + 5
    
    tag = Tag.objects.get(title=tag_name)
    
    if request.user.is_authenticated():
      all_posts = Post.objects.filter(is_public=True).filter(Q(groups__in=request.user.groups.all()) | Q(groups__isnull=True)).filter(tags=tag.id).order_by('-created_date')
    else:
      all_posts = Post.objects.filter(is_public=True).filter(groups__isnull=True).filter(tags=tag.id).order_by('-created_date')
    
    recent_posts = all_posts[start_index:end_index]
    num_pages = math.ceil(all_posts.count() / 5.0)
    
    display_page_nav = True
    if page_id == 1:
        if page_id == num_pages:
            display_page_nav = False
    
    # If invalid page number, redirect to home page
    if recent_posts.count() == 0:
      return redirect('/')
  
    for post in recent_posts:
      post.comment_list = Comment.objects.filter(post=post).filter(is_public=True)
    
    return render_to_response('blog/list.html', { 'recent_posts': recent_posts, 'page_id': page_id, 'num_pages': num_pages, 'display_page_nav': display_page_nav }, context_instance=RequestContext(request))

def detail(request, post_id):
    if request.user.is_authenticated():
        post = Post.objects.filter(is_public=True).filter(Q(groups__in=request.user.groups.all()) | Q(groups__isnull=True)).filter(id=post_id)
    else:
        post = Post.objects.filter(is_public=True).filter(groups__isnull=True).filter(id=post_id)
    
    if not post:
       return redirect('/blog/') #Invalid rights to access this post
    else:
        post = post[0]
        
    comment_list = Comment.objects.filter(post=post).filter(is_public=True).order_by('created_date')
    form = CommentForm()

    for c in comment_list:
      if c.author_id:
        u = User.objects.get(pk=c.author_id)
        c.author_name = u.username
        c.author_email = u.email
    
    return render_to_response('blog/detail.html', { 'post': post, 'comment_list': comment_list, 'form': form }, context_instance=RequestContext(request))

def comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if not request.user.is_authenticated():
                ak = Akismet(
                    key=settings.AKISMET_API_KEY,
                    blog_url='http://%s/' % Site.objects.get(pk=settings.SITE_ID).domain
                )
                if ak.verify_key():
                    data = {
                        'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
                        'user_agent': request.META.get('HTTP_USER_AGENT', ''),
                        'referrer': request.META.get('HTTP_REFERER', ''),
                        'comment_type': 'comment',
                        'comment_author': request.POST['author_name'].encode('utf-8'),
                        'comment_author_email': request.POST['author_email'].encode('utf-8'),
                    }
                    if ak.comment_check(request.POST['content'].encode('utf-8'), data=data, build_data=True):
                        return redirect('/blog/'+post_id+'/') # Invalid form entry
            #r = captcha.submit(request.POST['recaptcha_challenge_field'], request.POST['recaptcha_response_field'], settings.RECAPTCHA_PRIVATE_KEY, request.META['REMOTE_ADDR'])
            #if not r.is_valid:
            #    return redirect('/blog/'+post_id+'/') # Invalid form entry
            f = form.save(commit=False);
            
            f.post_id = post_id
            if request.user.is_authenticated():
                f.author_id = request.user.id
                f.author_name = ''
                f.author_email = ''
            f.save()
            
            # Send email notification
            email = EmailMessage('New Blog Comment - ginnibeam.net', 'You have a new comment at http://www.ginnibeam.net/blog/'+post_id+'/#comments', to=['vtbeam@gmail.com', 'alan@alanbeam.net'])
            email.send()
            
            return redirect('/blog/'+post_id+'/#comments') # Go back to blog with new comment
        else:
            return redirect('/blog/'+post_id+'/') # Invalid form entry
    else:
        return redirect('/blog/'+post_id+'/') # Go back to blog
