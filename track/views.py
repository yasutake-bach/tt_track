from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Boarding_record

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'

class Boarding_recordListView(LoginRequiredMixin, generic.ListView):
    model = Boarding_record
    template_name = 'boarding_record.html'

    def get_queryset(self):
        records = Boarding_record.objects.filter(user=self.request.user).order_by('-recording_start_date')
        return records