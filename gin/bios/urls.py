from django.conf.urls import patterns

urlpatterns = patterns('bios.views',
    (r'^$', 'index'),
    (r'^(?P<bio_name>[^/]+)$', 'detail')
)
