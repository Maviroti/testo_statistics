from rest_framework import serializers
from .models import Project, TestRun

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']

class TestRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestRun
        fields = [
            'id', 'project', 'product_version', 'start_time', 'end_time',
            'total_tests', 'passed_tests', 'failed_tests', 'failed_due_to_bugs', 'allure_report_url'
        ]
