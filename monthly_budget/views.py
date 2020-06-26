from django.shortcuts import render
from .models import AdministrativeBudget,MDABudget
from .serializers import administrativeBudgetSerializer,mdaBudgetSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# Create your views here.

"""
class based views for the model class and serializer class to help serialize the data output before 
presenting it..
"""
class administativeBudgetView(viewsets.ModelViewSet):

    """
    administrative view to give out all the data in the
    administrative model in a serialized way for easy implementation.
    """
    queryset = AdministrativeBudget.objects.all().order_by('-id')
    serializer_class = administrativeBudgetSerializer


class mdaBudgetView(viewsets.ModelViewSet):

    """
    MDABudget view to give out all the data in the
    MDABudget model in a serialized way for easy use.
    """

    queryset = MDABudget.objects.all().order_by('-id')
    serializer_class = mdaBudgetSerializer



"""
creating the api_root for the views to provide routes.
"""
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'administrativeBudget': reverse('administrative-list', request=request, format=format),
        'MDABudget': reverse('MDA-list', request=request, format=format),
    })