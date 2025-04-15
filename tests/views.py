from rest_framework import generics
from .models import Project, TestRun
from .serializers import ProjectSerializer, TestRunSerializer

class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TestRunCreateAPIView(generics.CreateAPIView):
    queryset = TestRun.objects.all()
    serializer_class = TestRunSerializer


from django.shortcuts import render, get_object_or_404
from .models import Project

def project_test_runs(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    test_runs = TestRun.objects.filter(project=project).order_by('-start_time')
    projects = Project.objects.all()
    return render(request, 'tests/project_test_runs.html', {
        'project': project,
        'test_runs': test_runs,
        'projects': projects,
    })

from django.shortcuts import render
from .models import Project

def index(request):
    projects = Project.objects.all()
    return render(request, 'tests/index.html', {'projects': projects})

