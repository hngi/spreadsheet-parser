from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import pandas
import xlrd
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
