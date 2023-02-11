from django import forms

class Boarding_recordForm(forms.Form):
    """乗車記録作成フォーム"""

    #user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    recording_start_date = forms.DateField(label='乗車開始日')
    recording_end_date = forms.DateField(label='乗車開始日', required=False)
    distance = forms.IntegerField(label='乗車距離', required=False)
    duration = forms.TimeField(label='乗車時間', required=False)
    title = forms.CharField(label='タイトル', max_length=30)
    height = forms.IntegerField(label='獲得標高', required=False)
    comment = forms.CharField(label='コメント', max_length=400, required=False)

    """latitude = forms.FloatField(label='緯度', required=False)
       longitude = forms.FloatField(label='経度', required=False)"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['recording_start_date'].widget.attrs['class'] = 'form-control'
        self.fields['recording_end_date'].widget.attrs['class'] = 'form-control'
        self.fields['distance'].widget.attrs['class'] = 'form-control'
        self.fields['duration'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['height'].widget.attrs['class'] = 'form-control'
        self.fields['comment'].widget.attrs['class'] = 'form-control'
        