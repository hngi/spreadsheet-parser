from django.contrib import admin
from .models import AdministrativeBudget,MDABudget
# Register your models here.
"""registering the models to the admin file"""

admin.site.register(AdministrativeBudget)
admin.site.register(MDABudget)