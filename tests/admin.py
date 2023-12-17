from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin



@admin.register(project_name_test)
class project_name_test_import_export(ImportExportModelAdmin):
  pass

@admin.register(Mp_location_test)
class Mp_location_test_import_export(ImportExportModelAdmin):
  pass

@admin.register(client_name_test)
class client_name_test_import_export(ImportExportModelAdmin):
  pass
