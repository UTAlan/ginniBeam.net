from django.conf.urls import patterns

urlpatterns = patterns('blog.views',
    (r'^$', 'index'),
    (r'^page/(?P<page_id>[\d]+)/$', 'index'),
    (r'^cat/(?P<cat_name>[^/]+)/$', 'category'),
    (r'^tag/(?P<cat_name>[^/]+)/page/(?P<page_id>[\d]+)/$', 'category'),
    (r'^tag/(?P<tag_name>[^/]+)/$', 'tag'),
    (r'^tag/(?P<tag_name>[^/]+)/page/(?P<page_id>[\d]+)/$', 'tag'),
    (r'^(?P<post_id>[\d]+)/$', 'detail'),
    (r'^(?P<post_id>[\d]+)/comment/$', 'comment'),
)
