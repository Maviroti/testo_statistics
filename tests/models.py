from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class TestRun(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='test_runs')
    product_version = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_tests = models.PositiveIntegerField()
    passed_tests = models.PositiveIntegerField()
    failed_tests = models.PositiveIntegerField()
    failed_due_to_bugs = models.PositiveIntegerField()

    @property
    def duration(self):
        return self.end_time - self.start_time

    @property
    def success_rate(self):
        if self.total_tests == 0:
            return 0
        return (self.passed_tests / self.total_tests) * 100

    @property
    def success_rate_excluding_bugs(self):
        tests_excluding_bugs = self.total_tests - self.failed_due_to_bugs
        if tests_excluding_bugs == 0:
            return 0
        return (self.passed_tests / tests_excluding_bugs) * 100

    @property
    def duration_seconds(self):
        return self.duration.total_seconds()

    def __str__(self):
        return f"{self.project.name} - {self.product_version} - {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}"
