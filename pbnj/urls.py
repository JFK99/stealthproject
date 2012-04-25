from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('pbnj.ideas_manager.views',
    url(r'^$', 'index', name='index'),
    url(r'^push', 'push', name='push'), 
	url(r'^pull', 'pull', name='pull'), 
	url(r'^vault', 'vault', name='vault'), 
	url(r'^login', 'login', name='login'), 
	url(r'^counter', 'count', name='counter'),
    url(r'^stats', 'stats', name='stats'),
    url(r'^dashboard/', direct_to_template, {'template': 'dashboard.html'}, name='dashboard'),
    # url(r'^pbnj/', include('pbnj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls))
)

urlpatterns += staticfiles_urlpatterns()