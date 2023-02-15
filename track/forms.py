from django import forms
from .models import Boarding_record, Photo, Plotting

class Boarding_recordForm(forms.ModelForm):
    """乗車記録作成フォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Boarding_record
        exclude = ('user',)

PhotoFormset = forms.inlineformset_factory(Boarding_record, Photo, fields='__all__', max_num=30)

PlottingFormset = forms.inlineformset_factory(Boarding_record, Plotting, fields='__all__', extra=1)
