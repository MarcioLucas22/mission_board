from . import models
from django import forms


class GoalForm(forms.ModelForm):
    class Meta:
        model = models.Goal
        fields = ['title', 'description', 'due_date', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        } # Estilização do formulário
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'due_date': 'Data de conclusão',
            'completed': 'Concluída',
        } # Alterando o label para ficar em português