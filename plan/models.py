from django.db import models


class Project(models.Model):
  recipient = models.CharField(max_length=6, primary_key=True)
  project_name = models.CharField(max_length=50)
  photo = models.ImageField(upload_to = f'project/%Y/%m/%d/', default = "static\images\default\project.jpg")
  displayfields = ['recipient','project_name']
  search_fields = ['recipient','project_name']
  list_filter = []
  def __str__(self):
      return f"{self.recipient} | {self.project_name}"
