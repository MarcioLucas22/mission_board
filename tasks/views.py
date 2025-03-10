from django.views.generic import ListView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect

class TasksListView(LoginRequiredMixin, ListView):
    model = models.Task
    context_object_name = 'tasks'
    template_name = 'task_list.html'

    def get_queryset(self): # Método que faz filtros pelo título da tarefa
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        priority = self.request.GET.get('priority')
        category = self.request.GET.get('category')

        print("title ", title)
        print("priority ", priority)
        print("category ", category)

        if title:
            queryset = queryset.filter(title__icontains=title)

        if priority:
            queryset = queryset.filter(priority=priority)

        if category:
            queryset = queryset.filter(category__id=category)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Pegando o contexto original
        context['tasks'] = models.Task.objects.filter(completed=False)
        context['categories'] = models.Category.objects.all()
        return context
    

class CompletedTasksView(LoginRequiredMixin, ListView):
    model = models.Task
    context_object_name = 'tasks'
    template_name = 'completed_tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(completed=True)
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = models.Task
    template_name = 'task_create.html'
    form_class = forms.TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Define o usuário logado como o autor da tarefa
        return super().form_valid(form)
    

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Task
    template_name = 'task_update.html'
    form_class = forms.TaskForm
    success_url = reverse_lazy('task_list')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')


class CompleteTaskView(LoginRequiredMixin, UpdateView):


    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if task.completed:
            task.completed = False
        else:
            task.completed = True

        task.save()
        return redirect('task_list')