from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rsa import verify
from .models import AddEvent

from event.forms import BookEventForm

# Create your views here.

def home(request):
    return render(request, 'event/home.html', {})

def contact(request):
    posts = AddEvent.objects.all()
    return render(request, 'event/contact.html', {'posts':posts})

def event(request):
    return render(request, 'event/event.html', {})

def about(request):
    return render(request, 'event/about.html', {})

def testingevents(request):
    events_list = AddEvent.objects.all()
    return render(request, 'event/testingevents.html', {'events_list':events_list})

def calender_view(request):
    Events = AddEvent.objects.all()
    for all_events in Events:
        print(all_events.id, all_events.title, all_events.date_posted)
    context = {'all_events':all_events}
    return render(request, 'event/calender_view.html', context)

    # Events = AddEvent.objects.all()
    # event_list = []
    # for event in Events:
    #         event_list.append(
    #             {
    #                 "title": Events.title,
    #                 "date_posted": Events.date_posted,
    #                 "detail": Events.detail
    #             }
    #         )
    # context = {'Events':Events}
    # return render(request, 'event/calender_view.html', context)

    # data = Events.filter(id=2)
    # print(Events.id)
    # # print(Events, data,"------------")
    # title = "Farewell"
    # date_posted = "January/2/2022"
    # detail = "detail"
    # context = {'title':title, 'date_posted':date_posted, 'detail':detail}

def book_event(request):
    if request.method == 'POST':
        form = BookEventForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'event/book_event.html', {})
    else:
        return render(request, 'event/book_event.html', {})
def view_event(request):
    posts = AddEvent.objects.all()
    return render(request, 'event/view_event.html', {'posts':posts})