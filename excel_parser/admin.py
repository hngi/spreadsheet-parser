from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Budget


@admin.register(Budget)
class ViewAdmin(ImportExportModelAdmin):
    pass
