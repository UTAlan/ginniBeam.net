from django.conf.urls import patterns

urlpatterns = patterns('quotes.views',
    (r'^$', 'index'),
)
