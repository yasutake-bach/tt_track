from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Boarding_record
from django.urls import reverse_lazy
from .forms import Boarding_recordForm

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'

class Boarding_recordListView(LoginRequiredMixin, generic.ListView):
    model = Boarding_record
    template_name = 'boarding_record.html'

    def get_queryset(self):
        records = Boarding_record.objects.filter(user=self.request.user).order_by('-recording_start_date')
        return records

class Boarding_recordCreateView(generic.FormView):
    template_name = 'boarding_record_create.html'
    form_class = Boarding_recordForm
    success_url = reverse_lazy('track:boarding-record')

    def form_valid(self, form):
            recording_start_date = forms.cleaned_data['recording_start_date']
            recording_end_date = forms.cleaned_data['recording_end_date']
            distance = forms.cleaned_data['distance']
            duration = forms.cleaned_data['duration']
            title = forms.cleaned_data['title']
            height = forms.cleaned_data['height']
            comment = forms.cleaned_data['comment']
            Boarding_record.objects.create(
                recording_start_date=recording_start_date,
                recording_end_date=recording_end_date,
                distance=distance,
                duration=duration,
                title=title,
                height=height,
                comment=comment,
            )
            return super().form_valid(form)