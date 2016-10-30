import django_filters
from SubTitlesApp.models import Flight
from SubTitlesApp.serializers import FlightSerializer
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters

## CRUDS

class FlightList(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class FlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

## Viewsets

class FlightsViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
