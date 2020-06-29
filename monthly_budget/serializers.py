# serializers convert the data in our db to and from js 
# and serve them unto our web pages

from rest_framework import serializers
<<<<<<< HEAD
from .models import AdministrativeBudget, MDABudget, EconomicExpenditure, EconomicRevenue, GovernmentFunctions
=======

from .models import (
    AdministrativeBudget,
    MDABudget,
    EconomicExpenditure,
    EconomicRevenue,
)

from .models import AdministrativeBudget, MDABudget, EconomicExpenditure, EconomicRevenue, GovernmentFunctions

>>>>>>> e5cf45b0ff12fc5b56196ee656409c8eb9375479


class AdministrativeExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrativeBudget

        fields = [
            "id",
            "sector",
            "budget",
            "allocation",
            "total_allocation",
            "balance",
        ]

        fields = ['id', 'sector', 'budget', 'allocation', 'total_allocation', 'balance', 'month']



class MDABudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MDABudget
<<<<<<< HEAD
        fields = ['id', 'mda', 'budget', 'allocation', 'total_allocation', 'balance', 'month']
=======

        fields = [
            "id",
            "mda",
            "budget",
            "allocation",
            "total_allocation",
            "balance",
        ]

        fields = ['id', 'mda', 'budget', 'allocation', 'total_allocation', 'balance', 'month']

>>>>>>> e5cf45b0ff12fc5b56196ee656409c8eb9375479


class EconomicExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicExpenditure
<<<<<<< HEAD
=======

        fields = "__all__"


class EconomicRevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicRevenue
        fields = (
            "id",
            "name",
            "revenue",
            "total_renue",
            "month",
        )

>>>>>>> e5cf45b0ff12fc5b56196ee656409c8eb9375479
        fields = ['id', 'name', 'budget', 'allocation', 'total_allocation', 'balance', 'month']
        

class GovernmentFunctionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernmentFunctions
        fields = ['id', 'name', 'budget', 'expenses', 'total_expenses', 'balance', 'month']
