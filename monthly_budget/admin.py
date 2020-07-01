from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from. models import AdministrativeBudget, MDABudget, EconomicRevenue, EconomicExpenditure, GovernmentFunctions


# Register your models here.

@admin.register(AdministrativeBudget)
class ViewAdmin(ImportExportModelAdmin):
    pass


@admin.register(MDABudget)
class ViewAdmin(ImportExportModelAdmin):
    pass


@admin.register(EconomicRevenue)
class ViewAdmin(ImportExportModelAdmin):
    pass


@admin.register(EconomicExpenditure)
class ViewAdmin(ImportExportModelAdmin):
    pass


@admin.register(GovernmentFunctions)
class ViewAdmin(ImportExportModelAdmin):
    pass
