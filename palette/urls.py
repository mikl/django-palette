from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'palette.views.index', name='palette-index'),
    url(r'^(?P<slug>[\w\d_-]+)/$', 'palette.views.palette_detail', name='palette-detail'),
)

