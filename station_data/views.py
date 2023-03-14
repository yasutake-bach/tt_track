from django.http import HttpResponse
from django.core.serializers import serialize



from .models import Station, Line, ConnectedStation, Company

# Create your views here.



def station_view(request):
    print(request.GET)
    queryset = Station.objects.all()

    if 'pref_cd' in request.GET:
        queryset = queryset.filter(pref_cd=request.GET['pref_cd'])

    if 'add' in request.GET:
        queryset = queryset.filter(add__contains=request.GET['add'])
    
    response = serialize('geojson', queryset, geometry_field='point')
    return HttpResponse(response, content_type='application/geo+json')
