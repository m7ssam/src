from django.db import models


# ----------------------------------- Planning ----------------------#

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
  
# ----------------------------------- Manpower ----------------------#

class Mp_location_test(models.Model):
   transaction = models.AutoField(primary_key=True)
   id = models.CharField(max_length=8 ,unique = True)
   name = models.CharField(max_length=100,blank=True, null=True)
   recipient = models.ForeignKey("project_name_test", on_delete=models.CASCADE)
   created = models.DateTimeField(auto_now = True)
   updated = models.DateTimeField(auto_now_add = True)
   def __str__(self):
      return f"{self.id} To {self.recipient}"

# ----------------------------------- Equipment ----------------------#
from django.core.validators import MaxValueValidator

class Eqp_list_test(models.Model):
   equn = models.IntegerField(validators=[MaxValueValidator(99999999)], primary_key = True)
   type = models.CharField(max_length=50)
   capacity = models.CharField(max_length=50)
   project = models.CharField(max_length=50)
   sap = models.CharField(max_length=50)
   recipient = models.CharField(max_length=8)
   date = models.DateField(auto_now=False, auto_now_add=False)
   kpi = models.FloatField(blank=True, null=True)
   efficiency = models.FloatField(blank=True, null=True)
   fail = models.IntegerField(blank=True, null=True)
   work = models.IntegerField(blank=True, null=True)
   rate = models.IntegerField(blank=True, null=True)
   dep = models.CharField(max_length=50)
   note = models.TextField(blank=True, null=True)
   def __str__(self):
      return (f"{self.equn} {self.type}")

