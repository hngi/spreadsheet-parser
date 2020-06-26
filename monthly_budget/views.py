from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from .models import MDABudget

class MDABudgetView(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = MDABudget.objects.all()
    serializer_class = MDABudgetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

