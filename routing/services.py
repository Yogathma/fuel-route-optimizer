import requests, polyline
from math import ceil
from dataclasses import dataclass
from .models import FuelStation

OSRM_URL = "https://router.project-osrm.org"
VEHICLE_RANGE = 500
MPG = 10
TANK_GALLONS = VEHICLE_RANGE / MPG

def miles(m): return m / 1609.34

@dataclass
class RouteResult:
    dist_m: float
    dur_s: float
    poly: str
    pts: list

def get_route(lat1, lng1, lat2, lng2):
    url = f"{OSRM_URL}/route/v1/driving/{lng1},{lat1};{lng2},{lat2}"
    r = requests.get(url, params={"overview":"full","geometries":"polyline"})
    data = r.json()["routes"][0]
    pts = polyline.decode(data["geometry"])
    return RouteResult(data["distance"], data["duration"], data["geometry"], pts)

def plan_fuel(route):
    dist = miles(route.dist_m)
    gallons = dist / MPG
    segments = ceil(dist / VEHICLE_RANGE)
    stops = max(segments - 1, 0)

    cheapest = FuelStation.objects.order_by("retail_price").first()
    if not cheapest:
        raise ValueError("CSV not loaded")

    price = cheapest.retail_price
    total_cost = gallons * price

    pts = route.pts
    fuel_stops = []

    for i in range(stops):
        frac = (i+1) / segments
        idx = int(frac * (len(pts)-1))
        lat, lng = pts[idx]
        pos = frac * dist
        g_here = min(TANK_GALLONS, gallons)
        c_here = g_here * price
        gallons -= g_here

        fuel_stops.append({
            "sequence": i+1,
            "approx_position_miles": round(pos,2),
            "map_location": {"lat":lat,"lng":lng},
            "truckstop": {
                "name":cheapest.name,
                "city":cheapest.city,
                "state":cheapest.state,
                "price":price
            },
            "gallons_purchased": round(g_here,2),
            "cost_usd": round(c_here,2)
        })

    return {
        "distance_miles": round(dist,2),
        "gallons_needed": round(dist/MPG,2),
        "price_per_gallon": round(price,3),
        "total_cost_usd": round(total_cost,2),
        "fuel_stops": fuel_stops
    }
