from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Project, TestRun
from .serializers import ProjectSerializer, TestRunSerializer

class ProjectListAPIView(generics.ListAPIView):
    """
    API endpoint для получения списка проектов.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TestRunListAPIView(generics.ListAPIView):
    """
    API endpoint для получения списка запусков тестов,
    отсортированных по дате начала (новые сверху).
    """
    queryset = TestRun.objects.all().order_by('-start_time')
    serializer_class = TestRunSerializer

class TestRunCreateAPIView(generics.CreateAPIView):
    """
    API endpoint для создания нового запуска тестов.
    """
    queryset = TestRun.objects.all()
    serializer_class = TestRunSerializer

def index(request):
    """
    Главная страница со списком проектов.
    """
    projects = Project.objects.all()
    return render(request, 'tests/index.html', {'projects': projects})

def project_test_runs(request, project_id):
    """
    Страница с запуском тестов для конкретного проекта.
    """
    project = get_object_or_404(Project, id=project_id)
    test_runs = TestRun.objects.filter(project=project).select_related('project').order_by('-start_time')
    projects = Project.objects.all()
    return render(request, 'tests/project_test_runs.html', {
        'project': project,
        'test_runs': test_runs,
        'projects': projects,
    })
