from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Boarding_record
from django.urls import reverse_lazy
from .forms import Boarding_recordForm, PhotoFormset, PlottingFormset
from django.shortcuts import render, redirect


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'

class Boarding_recordListView(LoginRequiredMixin, generic.ListView):
    model = Boarding_record
    template_name = 'boarding_record.html'

    def get_queryset(self):
        records = Boarding_record.objects.filter(user=self.request.user).order_by('-recording_start_date')
        return records

def add_boarding_record(request):
    form = Boarding_recordForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST' and form.is_valid():
        boarding_record = form.save(commit=False)
        boarding_record.user = request.user
        plotting_formset = PlottingFormset(request.POST, files=request.FILES, instance=boarding_record)
        photo_formset = PhotoFormset(request.POST, files=request.FILES, instance=boarding_record)

        if plotting_formset.is_valid() and photo_formset.is_valid(): 
            boarding_record.save()
            instances = plotting_formset.save(commit=False)
            for files in plotting_formset.deleted_objects:
                plotting_formset.delete()

            for files in instances:
                plotting_formset.save()
                
            photo_formset.save() 
            return redirect('track:boarding_record')

        # エラーメッセージつきのformsetをテンプレートへ渡すため、contextに格納
        else:
            context['plotting_formset'] = plotting_formset
            context['photo_formset'] = photo_formset 

    # GETのとき
    else:
        # 空のformsetをテンプレートへ渡す
        context['plotting_formset'] = PlottingFormset()
        context['photo_formset'] = PhotoFormset()

    return render(request, 'boarding_record_create.html', context)    


#def start_pref_station(request):


