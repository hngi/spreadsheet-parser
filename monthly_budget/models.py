from django.db import models

# Create your models here.

"""
This model is to parse the data from the SECTORS in the Monthly Administrative Excel file into the Database. Each 
variable correlates to a column in the Database and a Rows in the parsing excel file. The sector variable is to be 
filled with either one of the 5 sectors, budget variable is the Budget Amount budgeted for each Sector, allocation 
variable is the amount released into each sector for the month of MAY, total_allocation variable is the total amount 
released so far for each Sector, balance variable is the amount left from each Sector's Budget. The month variable 
automatically uploads the month
"""


class AdministrativeBudget(models.Model):
    sector = models.CharField(max_length=100, null=True)
    budget = models.FloatField(max_length=50, null=True)
    allocation = models.FloatField(max_length=50, null=True)
    total_allocation = models.FloatField(max_length=50, null=True)
    balance = models.FloatField(max_length=50, null=True)
    # month = models.real_time()

    def __str__(self):
        return self.sector


"""
This model is to parse the data from the MDA in the Monthly Administrative Excel file into the Database. Each 
variable correlates to a column in the Database and a Rows in the parsing excel file. The mda variable is to be 
filled with either of the mda in the excel file, budget variable is the Budget Amount budgeted for each mda, 
allocation variable is the amount released into for each mda for the month of MAY, total_allocation variable is the 
total amount released so far for each mda, balance variable is the amount left from each mda's Budget. The month variable 
automatically uploads the month
"""


class MDABudget(models.Model):
    mda = models.CharField(max_length=100, null=True)
    budget = models.FloatField(max_length=50, null=True)
    allocation = models.FloatField(max_length=50, null=True)
    total_allocation = models.FloatField(max_length=50, null=True)
    balance = models.FloatField(max_length=50, null=True)
    # month = models.real_time()

    def __str__(self):
        return self.mda
