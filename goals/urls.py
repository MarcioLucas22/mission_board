from django .urls import path
from . import views

urlpatterns = [
    path('goal/list/', views.GoalsView.as_view(), name='goal_list'),
    path('goal/create/', views.GoalCreateView.as_view(), name='goal_create'),
    path('goal/list/completed/', views.CompletedGoalView.as_view(), name='completed_goals'),
    path('goal/complete/<int:pk>/', views.CompleteGoalView.as_view(), name='complete_goal'),
    path('goal/update/<int:pk>/', views.GoalUpdateView.as_view(), name='goal_update'),
    path('goal/delete/<int:pk>/', views.GoalDeleteView.as_view(), name='goal_delete'),
]