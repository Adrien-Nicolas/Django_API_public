from rest_framework import serializers

from .models import Spot, User, Place, Opinion, User_Opinion, Place_Opinion, Presence

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pseudo', 'password', 'email', 'UID', 'isAdmin', 'isDelete')


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('name', 'latitude', 'longitude', 'precision', 'population', 'quality')


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = ('IDuser', 'IDplace', 'rating', 'comment', 'date')


class User_OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Opinion
        fields = ('IDuser', 'IDopinion')


class Place_OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place_Opinion
        fields = ('IDplace', 'IDopinion')


class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presence
        fields = ('IDuser', 'IDplace', 'date', 'timeStart', 'timeEnd')


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = ('__all__')



