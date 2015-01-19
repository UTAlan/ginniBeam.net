from django.conf.urls import patterns

urlpatterns = patterns('aboutme.views',
    (r'^$', 'index'),
)
