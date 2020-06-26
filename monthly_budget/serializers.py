from rest_framework import serializers
from .models import AdministrativeBudget,MDABudget

"""
Here is a serializer.py file to serialize all the data coming in from the models.py file
Here it is done using a Model class serializer which is easier and more effective.
The fields variable stores the model fields and also how it would display when it is query as well.
"""

class administrativeBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model =AdministrativeBudget
        fields =['sector','budget','allocation','total_allocation','balance']


class mdaBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MDABudget
        fields = ['mda','budget','allocation','total_allocation','balance']
