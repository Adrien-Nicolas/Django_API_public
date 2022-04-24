from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import UserSerializer, PlaceSerializer, OpinionSerializer, User_OpinionSerializer, Place_OpinionSerializer, PresenceSerializer
from .models import User, Place, Opinion, User_Opinion, Place_Opinion, Presence


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class OpinionViewSet(viewsets.ModelViewSet):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer

class User_OpinionViewSet(viewsets.ModelViewSet):
    queryset = User_Opinion.objects.all()
    serializer_class = User_OpinionSerializer

class Place_OpinionViewSet(viewsets.ModelViewSet):
    queryset = Place_Opinion.objects.all()
    serializer_class = Place_OpinionSerializer

class PresenceViewSet(viewsets.ModelViewSet):
    queryset = Presence.objects.all()
    serializer_class = PresenceSerializer


