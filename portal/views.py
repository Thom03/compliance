from django.shortcuts import render

from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.serializers import serialize

from .models import *

class MapData(TemplateView):
	template_name = "map.html"  


def viwandani_view(request):
    viwandani_as_geojson = serialize('geojson', Viwandani.objects.all())
    return HttpResponse(viwandani_as_geojson, content_type='json')	

def viwandanidata(request):
	construction = Viwandani.objects.all()
	
	return render(request,'tables.html', {'construction': construction})    