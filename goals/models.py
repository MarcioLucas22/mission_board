from django.db import models
from django.contrib.auth.models import User


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True) 
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

