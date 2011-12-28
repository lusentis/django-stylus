from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

import settings

urlpatterns = patterns('',
	url(r'^$', direct_to_template, {'template': 'index.html'}), 
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.STATIC_ROOT,
	}),
)

print ''.join(["Serving static contents from ", settings.STATIC_ROOT])

