from django.views.generic import (
    CreateView, UpdateView, DetailView, TemplateView, View, DeleteView)

class HomePage(TemplateView):

    template_name = 'index.html'
