
from django.http import Http404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from . import serializers
from .serializers import BudgetSerializer
from . import models
from .models import Budget


class BudgetViewSet(viewsets.ModelViewSet):
    """Handles Listing budget."""

    serializer_class = serializers.BudgetSerializer
    queryset = models.Budget.objects.all()
