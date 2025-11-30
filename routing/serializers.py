from rest_framework import serializers

class LocationSerializer(serializers.Serializer):
    lat = serializers.FloatField()
    lng = serializers.FloatField()

class RouteReqSerializer(serializers.Serializer):
    start = LocationSerializer()
    end = LocationSerializer()
