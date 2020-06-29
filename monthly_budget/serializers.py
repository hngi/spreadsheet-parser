# serializers convert the data in our db to and from js
# and serve them unto our web pages
from rest_framework import serializers
from .models import AdministrativeBudget, MDABudget, EconomicExpenditure, EconomicRevenue, GovernmentFunctions
<<<<<<< HEAD
from .models import (
    AdministrativeBudget,
    MDABudget,
    EconomicExpenditure,
    EconomicRevenue,
)
=======
>>>>>>> cf638bdd8bdb9d46a8750faa2082e791e4d8ae6b


class AdministrativeExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrativeBudget
<<<<<<< HEAD

        fields = [
            "id",
            "sector",
            "budget",
            "allocation",
            "total_allocation",
            "balance",
            "month",
        ]
=======
        fields = ['id', 'sector', 'budget', 'allocation', 'total_allocation', 'balance', 'month']
>>>>>>> cf638bdd8bdb9d46a8750faa2082e791e4d8ae6b


class MDABudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MDABudget
<<<<<<< HEAD
        fields = [
            "id",
            "mda",
            "budget",
            "allocation",
            "total_allocation",
            "balance",
            "month",
        ]


class EconomicRevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicRevenue
        fields = [
            "id",
            "name",
            "revenue",
            "total_revenue",
            "month",
        ]


class EconomicExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicExpenditure
        fields = [
            "id",
            "name",
            "budget",
            "allocation",
            "total_allocation",
            "balance",
            "month",
        ]


class GovernmentFunctionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernmentFunctions
        fields = [
            'id',
            'name',
            'budget',
            'expenses',
            'total_expenses',
            'balance',
            'month',
        ]
=======
        fields = ['id', 'mda', 'budget', 'allocation', 'total_allocation', 'balance', 'month']

class EconomicRevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicRevenue
        fields = [
            "id",
            "name",
            "revenue",
            "total_revenue",
            "month",
        ]

class EconomicExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicExpenditure
        fields = "__all__"


class GovernmentFunctionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernmentFunctions
        fields = "__all__"


class EconomicRevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicRevenue
        fields = "__all__"

>>>>>>> cf638bdd8bdb9d46a8750faa2082e791e4d8ae6b
