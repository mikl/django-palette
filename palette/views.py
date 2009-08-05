from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from palette.models import Palette

def index(request):
    tvars = {
        'palette_list': Palette.objects.select_related().all()
    }
    return render_to_response('palette/palette_index.html', tvars,
                              context_instance=RequestContext(request))



def palette_detail(request, slug):
    return index(request)

