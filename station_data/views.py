from django.http import HttpResponse
from django.core.serializers import serialize



from .models import Station, Line, ConnectedStation, Company

# Create your views here.



def station_view(request):
    print(request.GET)
    response = serialize('geojson', Station.objects.all(),
    geometry_field='point',
          )
    return HttpResponse(response, content_type='application/geo+json')
