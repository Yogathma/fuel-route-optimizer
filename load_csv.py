import csv, django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fuel_project.settings")
django.setup()

from routing.models import FuelStation

FuelStation.objects.all().delete()

with open("fuel-prices-for-be-assessment.csv") as f:
    r = csv.DictReader(f)
    for x in r:
        FuelStation.objects.update_or_create(
            opis_id=x["OPIS Truckstop ID"],
            defaults={
                "name": x["Truckstop Name"],
                "address": x["Address"],
                "city": x["City"],
                "state": x["State"],
                "retail_price": x["Retail Price"]
            }
        )

print("CSV LOADED SUCCESSFULLY")
