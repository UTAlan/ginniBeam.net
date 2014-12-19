from django.conf.urls import patterns

urlpatterns = patterns('lists.views',
    (r'^$', 'index'),
    (r'^namesongs/$', 'namesongs'),
    (r'^namesongs/names/(?P<name>[a-zA-Z])/$', 'list_names'),
    (r'^namesongs/names/(?P<name>[^/]+)/$', 'display_name'),
    (r'^namesongs/artists/(?P<artist>[0a-zA-Z])/$', 'list_artists'),
    (r'^namesongs/artists/(?P<artist>[^/]+)/$', 'display_artist'),
)
