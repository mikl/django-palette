from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'palette.views.index', name='palette-index'),
    url(r'^palette/(?P<slug>\w\d+)$', 'palette.views.palette_detail', name='palette-detail'),
)

