from django.conf.urls import patterns

urlpatterns = patterns('writings.views',
    (r'^$', 'index'),
    (r'^(?P<title>.+)/$', 'entry')
)
