<<<<<<< HEAD
from rest_framework import serializers
from .models import EconomicExpenditure
=======
# serializers convert the data in our db to and from js 
# and serve them unto our web pages

from rest_framework import serializers
from .models import AdministrativeBudget, MDABudget, EconomicExpenditure, EconomicRevenue


class AdministrativeExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrativeBudget
        fields = ['id', 'sector', 'budget', 'allocation', 'total_allocation', 'balance', 'month']


class MDABudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MDABudget
        fields = ['id', 'mda', 'budget', 'allocation', 'total_allocation', 'balance']
>>>>>>> 5f859841b3c08a21bf1950e3554f0562c74b3a91


class EconomicExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD
    	model = EconomicExpenditure
    	fields = "__all__"
=======
        model = EconomicExpenditure
        fields = "__all__"
        

>>>>>>> 5f859841b3c08a21bf1950e3554f0562c74b3a91
