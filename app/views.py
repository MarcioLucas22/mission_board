from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task
from goals.models import Goal
import json

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        
        # Contando as tarefas concluídas e não concluídas
        context['tasks_completed'] = json.dumps(Task.objects.filter(completed=True).count())
        context['tasks_not_completed'] = json.dumps(Task.objects.filter(completed=False).count())

        context['goals_completed'] = json.dumps(Goal.objects.filter(completed=True).count())
        context['goals_not_completed'] = json.dumps(Goal.objects.filter(completed=False).count())
        
        return context




class CustomLoginView(View):
    template_name = 'registration/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        return render(request, self.template_name, {'error': 'Usuário ou senha inválidos'})