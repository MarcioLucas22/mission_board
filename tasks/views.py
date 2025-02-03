from django.views.generic import ListView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.shortcuts import get_object_or_404, redirect

class TasksListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_list.html'

    def get_queryset(self): # Método que faz filtros pelo título da tarefa
        queryset = super().get_queryset()
        title = self.request.GET.get('title')

        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Pegando o contexto original
        context['tasks'] = Task.objects.all()
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_create.html'
    form_class = forms.TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Define o usuário logado como o autor da tarefa
        return super().form_valid(form)
    

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_update.html'
    form_class = forms.TaskForm
    success_url = reverse_lazy('task_list')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
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