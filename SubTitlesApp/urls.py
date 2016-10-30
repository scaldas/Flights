from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from SubTitlesApp import views
from SubTitlesApp.views import FlightsViewSet

router = DefaultRouter()
router.register(r'flights', FlightsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^flights/$', views.FlightList.as_view()),
    url(r'^flights/(?P<pk>[0-9]+)$', views.FlightDetail.as_view()),
]