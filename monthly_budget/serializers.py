from rest_framework import serializers
from .models import EconomicExpenditure


class EconomicExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicExpenditure
        fields = "__all__"
