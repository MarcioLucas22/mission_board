from . import models
from django import forms
from goals.models import Goal

class TaskForm(forms.ModelForm):

    class Meta:
        model = models.Task
        fields = ['title', 'description', 'category', 'goal', 'due_date', 'priority', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'goal': forms.Select(attrs={'class': 'form-select'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        } # Estilização do formulário
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'category': 'Categoria',
            'goal': 'Meta relacionada',
            'due_date': 'Data de vencimento',
            'priority': 'Prioridade',
            'completed': 'Concluído',
        } # Alterando o label para ficar em português

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['goal'].queryset = Goal.objects.filter(completed=False)