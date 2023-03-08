from django.urls import path

from . import views


app_name = 'station_data'
urlpatterns = [
    path('station/', views.station_view, name="station"),
]