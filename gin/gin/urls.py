from django.conf.urls import patterns, url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from feeds import LatestBlogs

admin.autodiscover()

feeds = {
    'latest': LatestBlogs,
}

urlpatterns = patterns('',
    (r'^$', 'blog.views.index'),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + 'images/' }),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    (r'^aboutme/', include('aboutme.urls')),
    (r'^blog/', include('blog.urls')),
    (r'^bios/', include('bios.urls')),
#    (r'^writings/', include('writings.urls')),
    (r'^lists/', include('lists.urls')),
#    (r'^photos/', include('photos.urls')),
    (r'^pics/', include('pics.urls')),
    (r'^quotes/', include('quotes.urls')),
    (r'^contact/', include('contact.urls')),
    (r'^yoga/', include('yoga.urls')),
    (r'^users/', include('users.urls')),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.Feed', {'feed_dict': feeds}),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }),
    )

