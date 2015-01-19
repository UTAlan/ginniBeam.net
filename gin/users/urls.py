from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name':'users/login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    (r'^register/$', 'users.views.registerUser'),
    (r'^edit/$', 'users.views.editUser'),
    (r'^password_reset/$', 'django.contrib.auth.views.password_reset', {'template_name':'users/password_reset_form.html'}),
    (r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', {'template_name':'users/password_reset_done.html'}),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'template_name':'users/password_reset_confirm.html'}),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', {'template_name':'users/password_reset_complete.html'}),
    (r'^password_change/$', 'django.contrib.auth.views.password_change', {'template_name':'users/password_change_form.html'}),
    (r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', {'template_name':'users/password_change_done.html'}),
)
