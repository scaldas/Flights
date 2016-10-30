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
import random

## CRUDS

class FlightList(generics.ListCreateAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer

class FlightDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer

## Viewsets
class FligthsDynamic(APIView):
	def get(self, request, format=None):
		vuelos = Flight.objects.all()
		serializer = FlightSerializer(vuelos, many=True)
		if len(serializer.data) < 3:
			return Response(serializer.data)
		else:
			vuelos_random = random.sample(serializer.data, 3)
			return Response(vuelos_random)

class FlightsViewSet(viewsets.ModelViewSet):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer
