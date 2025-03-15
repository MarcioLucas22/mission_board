from django .urls import path
from . import views

urlpatterns = [
    path('goal/list/', views.GoalsView.as_view(), name='goal_list'),
]