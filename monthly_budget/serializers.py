# serializers convert the data in our db to and from js
# and serve them unto our web pages
from rest_framework import serializers
from .models import AdministrativeBudget, MDABudget, EconomicExpenditure, EconomicRevenue, GovernmentFunctions
from .models import (
    AdministrativeBudget,
    MDABudget,
    EconomicExpenditure,
    EconomicRevenue,
)


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
            "month",
        ]


class MDABudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MDABudget
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
