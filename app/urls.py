from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('projects/', views.all_projects, name='projects'),
    path('new', views.create_project, name='create_project'),
    path('project/<int:pk>', views.show_project, name='show_project'),
    path('remove/<int:pk>', views.delete_project, name='delete_project'),
    path('upload/<int:pk>', views.add_files, name='add_files'),
]
