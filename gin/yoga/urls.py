from django.conf.urls import patterns

urlpatterns = patterns('yoga.views',
    (r'^$', 'index'),
)
