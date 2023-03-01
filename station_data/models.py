from django.db import models

# Create your models here.


class Company(models.Model):
    company_cd = models.IntegerField()
    #事業者コード		
    rr_cd = models.IntegerField()
    #鉄道コード		
    company_name = models.CharField(max_length=80)
    #事業者名(一般)	
    company_name_k = models.CharField(max_length=80, null=True, blank=True)
    #事業者名(一般・カナ)		
    company_name_h = models.CharField(max_length=80, null=True, blank=True)
    #事業者名(正式名称)	
    company_name_r = models.CharField(max_length=80, null=True, blank=True)
    #事業者名(略称)		
    company_url = models.URLField(null=True, blank=True)
    #Webサイト		
    company_type = models.IntegerField(null=True, blank=True)
    #事業者区分	
    e_status = models.IntegerField()
    #状態
    e_sort = models.IntegerField()
    #並び順	

    class Meta:
        verbose_name = 'Company'

    def __str__(self):
        return self.company_name

class Line(models.Model):
    line_cd = models.IntegerField()
    #路線コード	
    company_cd = models.IntegerField()
    #事業者コード	
    line_name = models.CharField(max_length=80)
    #路線名称(一般)	
    line_name_k = models.CharField(max_length=80, null=True, blank=True)
    #路線名称(一般・カナ)	
    line_name_h = models.CharField(max_length=80, null=True, blank=True)
    #路線名称(正式名称)	
    line_color_c = models.CharField(max_length=80, null=True, blank=True)
    #路線カラー（コード）	
    line_color_t = models.CharField(max_length=80, null=True, blank=True)
    #路線カラー(名称）	
    line_type = models.IntegerField(null=True, blank=True)
    #路線区分	
    lon = models.FloatField(null=True, blank=True)
    #路線表示時の中央経度	
    lat = models.FloatField(null=True, blank=True)
    #路線表示時の中央緯度	
    zoom = models.IntegerField()
    #路線表示時のGoogleMap倍率	
    e_status = models.IntegerField()
    #状態
    e_sort = models.IntegerField()
    #並び順	

    class Meta:
        verbose_name = 'Line'

    def __str__(self):
        return self.line_name

    


class Station(models.Model):
    station_cd = models.IntegerField()
    #駅コード	
    station_g_cd = models.IntegerField()
    #駅グループコード	
    station_name = models.CharField(max_length=80)
    #駅名称	
    station_name_k = models.CharField(max_length=80, null=True, blank=True)
    #駅名称(カナ)	
    station_name_r = models.CharField(max_length=200, null=True, blank=True)
    #駅名称(ローマ字)	
    line_cd = models.ForeignKey(Line, on_delete=models.CASCADE)
    #路線コード	
    pref_cd = models.IntegerField(null=True, blank=True)
    #都道府県コード	
    post = models.CharField(max_length=10, null=True, blank=True)
    #駅郵便番号	
    add = models.CharField(max_length=300, null=True, blank=True)
    #住所
    lon = models.FloatField(null=True, blank=True)
    #経度
    lat = models.FloatField(null=True, blank=True)
    #緯度
    open_ymd = models.DateField(null=True, blank=True)
    #開業年月日	
    close_ymd = models.DateField(null=True, blank=True)
    #廃止年月日	
    e_status = models.IntegerField(null=True, blank=True)
    #状態
    e_sort = models.IntegerField(null=True, blank=True)
    #並び順	

    class Meta:
        verbose_name = 'Station'

    def __str__(self):
        return self.station_name

class ConnectedStation(models.Model):
    line_cd = models.ForeignKey(Line, on_delete=models.CASCADE)
    #路線コード	
    station_cd1 = models.ManyToManyField(Station, related_name='station_cd1')
    #駅コード１	
    station_cd2 = models.ManyToManyField(Station,related_name='station_cd2')
    #駅コード２	

    class Meta:
        verbose_name = 'ConnectedStation'
