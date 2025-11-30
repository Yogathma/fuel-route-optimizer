from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RouteReqSerializer
from .services import get_route, plan_fuel, MPG, VEHICLE_RANGE

class TestView(APIView):
    def get(self, req):
        return Response({"msg": "API working da ✔️"})

class RouteView(APIView):
    def post(self, req):
        s = RouteReqSerializer(data=req.data)
        s.is_valid(raise_exception=True)

        st = s.validated_data["start"]
        en = s.validated_data["end"]

        route = get_route(st["lat"], st["lng"], en["lat"], en["lng"])
        fuel = plan_fuel(route)

        return Response({
            "summary": {
                "distance_miles": fuel["distance_miles"],
                "vehicle": {"range": VEHICLE_RANGE, "mpg": MPG},
                "fuel": fuel
            },
            "route": {"polyline": route.poly, "points": len(route.pts)},
            "fuel_stops": fuel["fuel_stops"]
        })
