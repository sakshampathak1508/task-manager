from django.urls import path
from . views import (
ProjectListApiView,ProjectApiView,ProjectCreateView, TaskListApiView,TaskApiView,TaskCreateView,
SubTaskApiView,SubTaskListApiView,SubTaskCreateView

)
urlpatterns = [
    path('all-projects/', ProjectListApiView.as_view()),
    path('project/<int:pk>/', ProjectApiView.as_view()),
    path('project/', ProjectCreateView.as_view()),
    path('task/',TaskListApiView.as_view()),
    path('task-add/',TaskCreateView.as_view()),
    path('task/<int:pk>/',TaskApiView.as_view()),
    path('sub-task/',SubTaskListApiView.as_view()),
    path('sub-task-add/',SubTaskCreateView.as_view()),
    path('sub-task/<int:pk>/',SubTaskApiView.as_view()),
]
