# from django.urls import path
# from . import views

# urlpatterns = [
#     path('api/projects/', views.ProjectListAPIView.as_view(), name='api-projects'),
#     path('api/testruns/', views.TestRunCreateAPIView.as_view(), name='api-testrun-create'),
#     path('projects/<int:project_id>/', views.project_test_runs, name='project-test-runs'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # главная страница со списком проектов
    path('api/projects/', views.ProjectListAPIView.as_view(), name='api-projects'),
    path('api/testruns/', views.TestRunCreateAPIView.as_view(), name='api-testrun-create'),
    path('projects/<int:project_id>/', views.project_test_runs, name='project-test-runs'),
]
