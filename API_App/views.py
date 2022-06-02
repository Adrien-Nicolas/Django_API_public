import json
import copy
from mimetypes import init
import string
from urllib import request
from django.shortcuts import render
from sklearn.cluster import KMeans
import sklearn.mixture
import numpy as np
import pandas as pd
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status    
#from shapely.geometry import Point, Polygon, MultiPoint
from django.contrib.gis.geos import Point, Polygon
from shapely.ops import nearest_points
from collections import Counter

from .serializers import UserSerializer, PlaceSerializer, OpinionSerializer, User_OpinionSerializer, Place_OpinionSerializer, PresenceSerializer, SpotSerializer
from .models import User, Place, Opinion, User_Opinion, Place_Opinion, Presence, Spot
from . import serializers

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

class SpotViewSet(APIView):
    
    def get(self, request, format=None,pk=None):
        if pk is not None:
            spot = Spot.objects.get(pk=pk)
            serializer = SpotSerializer(spot)
            print("here")
            return Response(serializer.data)
        else:
            spot = Spot.objects.all().order_by("?").first()
            spot.locker = True
            spot.save()

            serializer = SpotSerializer(spot)
            return Response(serializer.data)
        


    def post(self, request, format=None,pk=None):
        points = {"coordinates":[],"properties":{},"type":""}
        points_a=[]
        i=0
        if not pk:
            return Response({"error":"no id"},status=status.HTTP_400_BAD_REQUEST)
        
        northEastLat = request.GET["northEastLat"]
        northEastLong = request.GET["northEastLong"]
        southWestLat = request.GET["southWestLat"]
        southWestLong = request.GET["southWestLong"]

        if northEastLat and northEastLong and southWestLat and southWestLong:
            northEast = Point(float(northEastLong), float(northEastLat))
            southWest = Point(float(southWestLong), float(southWestLat))
            northWest = Point(float(southWestLong), float(northEastLat))
            southEast = Point(float(northEastLong), float(southWestLat))
            polygon = Polygon(((northEast.coords[0],northEast.coords[1]), (southWest.coords[0],southWest.coords[1]), (northWest.coords[0],northWest.coords[1]), (southEast.coords[0],southEast.coords[1]), (northEast.coords[0],northEast.coords[1]))) 

            pointCoord = Spot.objects.filter(point_coord_spot__within=polygon)
            kmeans = sklearn.cluster.AffinityPropagation(random_state = 0).fit(pointCoord.values_list('point_coord_spot',flat=True))
            labels = kmeans.labels_

            cluster_center = kmeans.cluster_centers_

            counter_labels = Counter(labels).items()
            dic_counter_labels = dict(counter_labels)
            keys_values = dic_counter_labels.items()

            new_dict_counter_labels = {str(key): int(value) for key, value in keys_values}

            for key in dic_counter_labels:
                if dic_counter_labels[key]>1: 
                    points["coordinates"]=cluster_center[key]
                    points["properties"]["cluster_id"]=(key)
                    points["properties"]["cluster_size"]=(dic_counter_labels[key])
                    points["type"]="Cluster"
                    points_a.append(copy.deepcopy(points))
                else:
                    index_point = list(labels).index(key)
                    point_object = pointCoord[index_point]
                    points["coordinates"]=point_object.point_coord_spot.coords
                    points["properties"]["spot_point_id"]=int(point_object.id)
                    points["type_equipement"]=point_object.typequipement
                    points["type"]="Spot_Point"
                    points_a.append(copy.deepcopy(points))


            #return Response({'cluster_data':new_dict_counter_labels, 'spots':serializer.data})

            return Response({'Points': points_a})
        else:
            return Response({"error":"no coords"},status=status.HTTP_400_BAD_REQUEST)
    


    def put(self, request, format=None,pk=None):
        if not pk:
            return Response({"error":"no id"},status=status.HTTP_400_BAD_REQUEST)
        spot = Spot.objects.get(pk=pk)
        spot.locker = False
        spot.save()
        return Response({"success":"ok"},status=status.HTTP_200_OK)
    
    def delete(self, request, format=None,pk=None):
        if not pk:
            return Response({"error":"no id"},status=status.HTTP_400_BAD_REQUEST)
        spot = Spot.objects.get(pk=pk)
        spot.delete()
        return Response({"success":"ok"},status=status.HTTP_200_OK)
    


        

      

