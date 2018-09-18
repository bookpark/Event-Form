from django.shortcuts import render, get_object_or_404

from events.models import Event


def event_list(request):
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'event_list.html', context)


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {
        'event': event,
    }
    return render(request, 'event_detail.html', context)
