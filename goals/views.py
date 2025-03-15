from django.shortcuts import render
from . import models
from django.views.generic import ListView
from django.urls import reverse_lazy


class GoalsView(ListView):
    model = models.Goal
    context_object_name = 'goals'
    template_name = 'goal_list.html'
    success_url = reverse_lazy('goal_list')
