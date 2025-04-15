from django.contrib import admin
from .models import Project, TestRun

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(TestRun)
class TestRunAdmin(admin.ModelAdmin):
    list_display = (
        'project', 'product_version', 'start_time', 'end_time',
        'total_tests', 'passed_tests', 'failed_tests', 'failed_due_to_bugs'
    )
    list_filter = ('project', 'product_version')
    search_fields = ('product_version',)
    date_hierarchy = 'start_time'
