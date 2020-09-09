from django.shortcuts import render
from .models import FarmerProfile
from .serializers import GroupSerializer, FarmerProfileSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class FarmerListView():

    template_name = 'farmers_list.html'
