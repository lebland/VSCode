from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Event
from datetime import datetime
import pytz


def register(request):
    """Simple registration view that accepts name and email and shows a thank-you message.
    This does not persist data — it simply demonstrates a basic form flow.
    """
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        # In a real app you'd validate and save these values.
        context['submitted'] = True
        context['name'] = name or None
        context['email'] = email or None
        context['message'] = message or None
    return render(request, 'register.html', context)


class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        # Filtrer les événements futurs par défaut
        return Event.objects.filter(date__gte=datetime.now(pytz.UTC)).order_by('date')


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'


class EventCreateView(CreateView):
    model = Event
    template_name = 'events/event_form.html'
    fields = ['title', 'date', 'location', 'description']
    
    def get_success_url(self):
        messages.success(self.request, "L'événement a été créé avec succès.")
        return reverse_lazy('event-list')


class EventUpdateView(UpdateView):
    model = Event
    template_name = 'events/event_form.html'
    fields = ['title', 'date', 'location', 'description']
    
    def get_success_url(self):
        messages.success(self.request, "L'événement a été modifié avec succès.")
        return reverse_lazy('event-list')


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event-list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, "L'événement a été supprimé.")
        return super().delete(request, *args, **kwargs)
