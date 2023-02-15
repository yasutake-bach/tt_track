from django.contrib import admin
from .models import Boarding_record, Photo, Plotting
# Register your models here.
#admin.site.register(Boarding_record)
admin.site.register(Photo)
admin.site.register(Plotting)
#admin.site.register(CustomUser)

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


class PlottingInline(admin.StackedInline):
    model = Plotting
    extra = 1


class BoardingRecordCreateAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, PlottingInline]

admin.site.register(Boarding_record, BoardingRecordCreateAdmin)

