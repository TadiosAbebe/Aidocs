from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Project, ProjectFile
from .helpers import pdf_to_text
from django.db.models import Q
import shutil
from django.contrib.auth.models import User


def home(request):
    content = {'title': 'AIDOCS'}
    return render(request, "index.html", content)


def all_projects(request):
    if request.user.is_authenticated:
        user = request.user
        projects = Project.objects.filter(Q(user=user) | Q(title='Plagiarism Analysis Database'))
        content = {
            'projects': projects,
            'title': 'Projects',
        }
        return render(request, "pages/project_list.html", content)
    return render(request, "pages/project_list.html")


def create_project(request):
    if request.method == 'POST':
        name = request.POST['name']
        if request.user.is_authenticated:
            user = request.user
            project = Project(title=name, user=user)
            project.save()
            files = request.FILES.getlist('files')
            add_files_to_project(files, project)
            return redirect('projects')
    content = {
        'title': 'New Project'
    }
    return render(request, "pages/project_new.html", content)


def add_files_to_project(files, project):
    for file in files:
        if file.name.endswith('.pdf'):
            file_instance = ProjectFile(project=project)
            file_instance.file_pdf = file
            file = pdf_to_text(file)
            file_instance.file = file
            file_instance.save()
        elif file.name.endswith('.txt'):
            file_instance = ProjectFile(file=file, project=project)
            file_instance.save()


def show_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    content = {
        "projects": reverse('projects'),
        "project": project,
        "title": project.title,
    }
    return render(request, "pages/project_edit.html", content)


def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_folder = f'data/projects/{project.project_folder}'
    try:
        shutil.rmtree(project_folder)
    except FileNotFoundError:
        pass
    finally:
        pass
    project.delete()
    return redirect('projects')


def add_files(request, pk):
    if request.method == 'POST':
        print("sup")
        project = get_object_or_404(Project, pk=pk)
        files = request.FILES.getlist('files')
        add_files_to_project(files, project)
        return redirect('show_project', pk=pk)
    return None
