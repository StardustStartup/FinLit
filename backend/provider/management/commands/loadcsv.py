from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import GEOSGeometry, Point
from provider.models import Incident, IncidentType
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        cfile = "willcsv.csv"
        i = 0
        with open(cfile) as csvfile:
            readCSV = csv.reader(csvfile, skipinitialspace=True, delimiter=', ')
            for row in readCSV:
                incident = Incident(type=int(row[3]), month=int(row[4])+1, location=Point(float(row[0]), float(row[1])))
                try:
                    incident.save()
                except:
                    print("error at line", str(i))
                i += 1