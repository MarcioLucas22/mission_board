from django.db import models

class Goal(models.Model):
    TIMEFRAME_CHOICES = [
        ('short', 'Curto Prazo'),
        ('medium', 'Médio Prazo'),
        ('long', 'Longo Prazo'),
    ]

    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    timeframe = models.CharField(max_length=10, choices=TIMEFRAME_CHOICES)
    progress = models.FloatField(default=0.0)  # Representa o percentual concluído
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class GoalTask(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="tasks")
    task = models.ForeignKey("tasks.Task", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.goal.title} - {self.task.title}"

