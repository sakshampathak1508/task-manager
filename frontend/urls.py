from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index),
    path('project/<int:pk>', views.project),
    path('project/create', views.project_create),
    path('project/<int:pk>/edit', views.project_edit),
    path('project/<int:pk>/delete', views.project_delete),
    path('project/<int:pk1>/task/<int:pk2>/', views.task),
    path('project/<int:pk1>/task/<int:pk2>/edit', views.task_edit),
    path('project/<int:pk>/task/create', views.task_create),
    path('project/<int:pk1>/task/<int:pk2>/delete', views.task_delete),
]
