from rest_framework import serializers
from .models import Budget


class Rend(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['MDA_name','project_recipient_name','project_name','project_amount']
