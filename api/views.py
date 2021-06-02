from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import SurveySerializer
from .models import Survey
# Create your views here.
# contains all of your endpoints- locations on the web server i.e. website.com/api


# will return all of the surveys in the application
class SurveyView(generics.CreateAPIView):

    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
