from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),


        # REST API endpoints
    path('api/', views.apiOverview, name="api-overview"),
    path('api/task-list/', views.taskList, name="task-list"),
    path('api/task-detail/<int:pk>/', views.taskDetail, name="task-detail"),
    path('api/task-create/', views.taskCreate, name="task-create"),
    path('api/task-update/<int:pk>/', views.taskUpdate, name="task-update"),
    path('api/task-delete/<int:pk>/', views.taskDelete, name="task-delete"),
    
]

