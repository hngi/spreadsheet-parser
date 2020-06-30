# serializers convert the data in our db to and from js
# and serve them unto our web pages
from rest_framework import serializers
from .models import AdministrativeBudget, MDABudget, EconomicExpenditure, EconomicRevenue, GovernmentFunctions
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 53415df672d7a6d0c95c64fd127b716754fc5457
from .models import (
    AdministrativeBudget,
    MDABudget,
    EconomicExpenditure,
    EconomicRevenue,
)
<<<<<<< HEAD
=======
=======
>>>>>>> cf638bdd8bdb9d46a8750faa2082e791e4d8ae6b
>>>>>>> 53415df672d7a6d0c95c64fd127b716754fc5457


class AdministrativeExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrativeBudget
<<<<<<< HEAD
=======
<<<<<<< HEAD

>>>>>>> 53415df672d7a6d0c95c64fd127b716754fc5457
        fields = [
            "id",
            "sector",
            "budget",
            "allocation",
            "total_allocation",
            "balance",
            "month",
        ]
<<<<<<< HEAD
=======
=======
        fields = ['id', 'sector', 'budget', 'allocation', 'total_allocation', 'balance', 'month']
>>>>>>> cf638bdd8bdb9d46a8750faa2082e791e4d8ae6b
>>>>>>> 53415df672d7a6d0c95c64fd127b716754fc5457


class MDABudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MDABudget
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 53415df672d7a6d0c95c64fd127b716754fc5457
        fields = [
            "id",
            "mda",
            "budget",
            "allocation",
            "total_allocation",
            "balance",
            "month",
        ]
<<<<<<< HEAD
=======


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
>>>>>>> 53415df672d7a6d0c95c64fd127b716754fc5457


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
<<<<<<< HEAD
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
        model = EconomicRevenue
        fields = "__all__"

>>>>>>> cf638bdd8bdb9d46a8750faa2082e791e4d8ae6b
>>>>>>> 53415df672d7a6d0c95c64fd127b716754fc5457
