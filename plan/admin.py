from django.contrib import admin

from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Project)
class Mp_list_import_export(ImportExportModelAdmin,admin.ModelAdmin):
  list_display = Project.displayfields
  search_fields = Project.search_fields
  list_filter = Project.list_filter
  pass
