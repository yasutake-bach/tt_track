from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Boarding_record(models.Model):
    """乗車記録モデル"""

    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    recording_start_date = models.DateField()
    recording_end_date = models.DateField(null=True, blank=True)
    distance = models.IntegerField(default=0)
    duration = models.TimeField(null=True, blank=True)
    title = models.CharField(max_length=30)
    height = models.IntegerField(default=0)
    comment = models.CharField(max_length=400, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    """写真モデル"""
    boarding_record = models.ForeignKey(Boarding_record, on_delete=models.CASCADE, null=True, default=None)
    photo = models.ImageField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    """def __str__(self):
        return self.title"""


class Plotting(models.Model):
    """ルート作成モデル"""
    boarding_record = models.ForeignKey(Boarding_record, on_delete=models.CASCADE, null=True, default=None)
    latitude = models.FloatField(default=None, null=True, blank=True)
    longitude = models.FloatField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


   

