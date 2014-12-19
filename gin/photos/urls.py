from django.conf.urls import patterns

urlpatterns = patterns('photos.views',
    (r'^$', 'index'),
    (r'^page/(?P<page_id>[0-9]+)/$', 'index'),
    (r'^(?P<gallery_name>[^/]+)/$', 'gallery'),
    (r'^(?P<gallery_name>[^/]+)/page/(?P<page_id>[0-9]+)/$', 'gallery'),
    (r'^(?P<gallery_name>[^/]+)/(?P<photo_id>[^/]+)/$', 'photo'),
    (r'^(?P<gallery_name>[^/]+)/(?P<photo_id>[^/]+)/comment/$', 'comment'),
)
