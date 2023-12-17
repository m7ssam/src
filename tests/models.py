from django.db import models

class project_name_test(models.Model):
  recipient = models.CharField(max_length=6, primary_key=True)
  project_name = models.CharField(max_length=50)
  client_name = models.ForeignKey('client_name_test', on_delete=models.CASCADE)
  class Meta:
    ordering = ["recipient"]
  def __str__(self):
      return f"{self.recipient} | {self.project_name}"


class client_name_test(models.Model):
  client_id = models.AutoField(primary_key=True)
  client_name = models.CharField(max_length=50)
  def __str__(self):
      return f"{self.client_id} | {self.client_name}"
  

class Mp_location_test(models.Model):
   transaction = models.AutoField(primary_key=True)
   id = models.CharField(max_length=8 ,unique = True)
   name = models.CharField(max_length=100,blank=True, null=True)
   recipient = models.ForeignKey("project_name_test", on_delete=models.CASCADE)
   created = models.DateTimeField(auto_now = True)
   updated = models.DateTimeField(auto_now_add = True)
   def __str__(self):
      return f"{self.id} To {self.recipient}"
   