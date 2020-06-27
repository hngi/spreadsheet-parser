<<<<<<< HEAD
# serializers convert the data in our db to and from js 
# and serve them unto our web pages

from rest_framework import serializers
from .models import AdministrativeBudget, MDABudget,  EconomicExpenditure


class AdministrativeExpensesSerializer(serializers.ModelSerializer):
	class Meta:
		model = AdministrativeBudget
        fields = ['id', 'sector', 'budget', 'allocation', 'total_allocation', 'balance']


class MDABudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MDABudget
        fields = ['id', 'mda', 'budget', 'allocation', 'total_allocation', 'balance']


class EconomicExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicExpenditure
        fields = "__all__"
        
=======
from rest_framework import serializers
from .models import EconomicExpenditure


class EconomicExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicExpenditure
        fields = "__all__"
<<<<<<< HEAD
=======
>>>>>>> 442756fa9aba71db5ac4a82753e2e51feeaa0cea
>>>>>>> 387210e0212fe7fdb24dc982b5634138b2fa935b
