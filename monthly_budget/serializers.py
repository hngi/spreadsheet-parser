# serializers convert the data in our db to and from js 
# and serve them unto our web pages

from rest_framework import serializers
from .models import AdministrativeBudget, MDABudget


class AdministrativeExpensesSerializer(serializers.ModelSerializer):
	class Meta:
		model = AdministrativeBudget
        fields = ['id', 'sector', 'budget', 'allocation', 'total_allocation', 'balance']


class MDABudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MDABudget
        fields = ['id', 'mda', 'budget', 'allocation', 'total_allocation', 'balance']
        