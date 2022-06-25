from django.db import models
from app.models import Project
import json

class Report(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='sim_project')
    algorithm = models.CharField(max_length=100)
    all_data = models.TextField()
    selected_document_index = models.IntegerField()
    selected_document_name = models.CharField(max_length=1024)

    def get_output(self):
        return json.loads(self.all_data)
