# serializers convert the data in our db to and from js 
# and serve them unto our web pages 

from rest_framework import serializers
from .models import Budget

class BudgetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Budget
		fields = ('id', 'MDA_name', 'project_recipient_name', 'project_name', 'project_amount', 'project_date')
