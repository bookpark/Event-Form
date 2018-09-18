from django.shortcuts import render, get_object_or_404, redirect

from events.forms import ApplicationForm
from events.models import Event


def event_list(request):
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'event_list.html', context)


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    application_form = ApplicationForm()
    context = {
        'event': event,
        'form': application_form,
    }
    return render(request, 'event_detail.html', context)


def event_apply(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.event = event
            application.save()
            return redirect('event-detail', pk=event.pk)
