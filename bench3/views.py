# cal/views.py

from datetime import datetime, date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta
import calendar
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


from .models import *
from .utils import bench3
from .forms import EventForm #, AddMemberForm

@login_required(login_url='signup')
# def index(request):
#     return HttpResponse('hello')
def index(request):
    if request.user.is_anonymous:
        return redirect("/signup")
    return render(request,'index.html')

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

class CalendarView(LoginRequiredMixin, generic.ListView):
    login_url = 'signup'
    model = Reservation3
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = bench3(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

@login_required(login_url='signup')
def create_event(request):    
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        name = form.cleaned_data['title']
        description = form.cleaned_data['description']
        start_time = form.cleaned_data['start_time']
        end_time = form.cleaned_data['end_time']
        Reservation3.objects.get_or_create(
            # user=request.user,
            name=name,
            description=description,
            start_time=start_time,
            end_time=end_time
        )
        return HttpResponseRedirect(reverse('calendarapp:calendar'))
    return render(request, 'event.html', {'form': form})

class EventEdit(generic.UpdateView):
    model = Reservation3
    fields = ['name', 'description', 'start_time', 'end_time']
    template_name = 'event.html'

@login_required(login_url='signup')
def event_details(request, event_id):
    event = Reservation3.objects.get(id=event_id)
    # eventmember = EventMember1.objects.filter(event=event)
    context = {
        'event': event,
        # 'eventmember': eventmember
    }
    return render(request, 'event-details.html', context)


# def add_eventmember(request, event_id):
#     forms = AddMemberForm()
#     if request.method == 'POST':
#         forms = AddMemberForm(request.POST)
#         if forms.is_valid():
#             member = EventMember1.objects.filter(event=event_id)
#             event = Event1.objects.get(id=event_id)
#             if member.count() <= 9:
#                 user = forms.cleaned_data['user']
#                 EventMember1.objects.create(
#                     event=event,
#                     user=user
#                 )
#                 return redirect('calendarapp:calendar')
#             else:
#                 print('--------------User limit exceed!-----------------')
#     context = {
#         'form': forms
#     }
#     return render(request, 'add_member.html', context)

# class EventMemberDeleteView(generic.DeleteView):
#     model = EventMember1
#     template_name = 'event_delete.html'
#     success_url = reverse_lazy('calendarapp:calendar')