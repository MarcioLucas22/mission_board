from django.shortcuts import render
from . import models
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms


class GoalsView(LoginRequiredMixin, ListView):
    model = models.Goal
    context_object_name = 'goals'
    template_name = 'goal_list.html'
    success_url = reverse_lazy('goal_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goals'] = models.Goal.objects.filter(completed=False)
        return context
    

class GoalCreateView(LoginRequiredMixin, CreateView):
    model = models.Goal
    template_name = 'goal_create.html'
    form_class = forms.GoalForm
    success_url = reverse_lazy('goal_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Define o usuário logado como o autor da meta
        return super().form_valid(form)
    

class GoalUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Goal
    template_name = 'goal_update.html'
    form_class = forms.GoalForm
    success_url = reverse_lazy('goal_list')


class GoalDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Goal
    template_name = 'goal_delete.html'
    success_url = reverse_lazy('goal_list')


class CompleteGoalView(LoginRequiredMixin, UpdateView):


    def post(self, request, pk):
        goal = get_object_or_404(models.Goal, pk=pk)
        if goal.completed:
            goal.completed = False
        else:
            goal.completed = True

        goal.save()
        return redirect('goal_list')
    

class CompletedGoalView(LoginRequiredMixin, ListView):
    model = models.Goal
    context_object_name = 'goals'
    template_name = 'completed_goals.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goals'] = models.Goal.objects.filter(completed=True)
        return context