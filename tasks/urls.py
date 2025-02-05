from django .urls import path
from . import views

urlpatterns = [
    path('task/list/', views.TasksListView.as_view(), name='task_list'),
    path('task/list/completed/', views.CompletedTasksView.as_view(), name='completed_tasks'),
    path('task/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task/complete/<int:pk>/', views.CompleteTaskView.as_view(), name='complete_task'),
    path('task/update/<int:pk>/', views.TaskUpdateView.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task_delete'),
]