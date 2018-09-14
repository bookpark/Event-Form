from django.shortcuts import render

from events.models import Event


def event_list(request):
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'event_list.html', context)
