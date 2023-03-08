from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
from .models import Station, Line, ConnectedStation, Company
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

# Register your models here.

class CompanyResource(resources.ModelResource):
    class Meta:
        model = Company
        import_id_fields = ('company_cd',)

class StationResource(resources.ModelResource):
        line_cd = fields.Field(
                attribute='line_cd',
                widget=ForeignKeyWidget(Line, field='line_cd')
        )
        add = fields.Field(
                attribute='add',
                column_name='address',
        )

        def before_import_row(self, row, row_number=None, **kwargs):
                if  row['open_ymd'] == '0000-00-00':
                    row['open_ymd'] = None

                if  row['close_ymd'] == '0000-00-00':
                    row['close_ymd'] = None

        
        class Meta:
                model = Station
                import_id_fields = ('station_cd',)
                #exclude = ('open_ymd', 'close_ymd' )


class LineResource(resources.ModelResource):
        company_cd = fields.Field(
                attribute='company_cd',
                widget=ForeignKeyWidget(Company, field='company_cd')
        )
        class Meta:
                model = Line
                import_id_fields = ('line_cd',)


class ConnecteStationdResource(resources.ModelResource):
        station_cd1 = fields.Field(
                column_name= 'station_cd1',
                attribute='station_cd1',
                widget=ManyToManyWidget(Station, field='station_cd')
        )

        station_cd2 = fields.Field(
                column_name= 'station_cd2',
                attribute='station_cd2',
                widget=ManyToManyWidget(Station, field='station_cd')
        )
        line_cd = fields.Field(
                attribute='line_cd',
                widget=ForeignKeyWidget(Line, field='line_cd')
        )

        class Meta:
                model = ConnectedStation
                exclude = ('station_cd2')
               

@admin.register(Company)
class CompanyAdmin(ImportExportModelAdmin):
        resource_class = CompanyResource

@admin.register(Station)
class StationAdmin(ImportExportModelAdmin):
        resource_class = StationResource

@admin.register(Line)
class LineAdmin(ImportExportModelAdmin):
        resource_class = LineResource

@admin.register(ConnectedStation)
class ConnectedStationAdmin(ImportExportModelAdmin):
        resource_class = ConnecteStationdResource

