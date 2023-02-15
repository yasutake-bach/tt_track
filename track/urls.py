from django.urls import path

from . import views


app_name = 'track'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('boarding-record/', views.Boarding_recordListView.as_view(), name="boarding_record"),
    path('boarding-record-create/', views.add_boarding_record, name="boarding_record_create"),
]