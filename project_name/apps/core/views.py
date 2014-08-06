# -*- coding: utf-8 -*-

from django.views.generic import ListView, DetailView, CreateView, DeleteView, \
    UpdateView

from .forms import ModelNameForm
from .models import ModelName


class ModelNameListView(ListView):
    model = ModelName


class ModelNameDetailView(DetailView):
    model = ModelName


class ModelNameCreateView(CreateView):
    model = ModelName
    form_class = ModelNameForm


class ModelNameDeleteView(DeleteView):
    model = ModelName


class ModelNameUpdateView(UpdateView):
    model = ModelName
    form_class = ModelNameForm
