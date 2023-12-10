# load_data_from_csv.py
from django.core.management.base import BaseCommand, CommandError
from tourlist.models import Tourmodel
import csv

class Command(BaseCommand):
    help = 'Load data from CSV file into Database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The csv file to load data from')

    def handle(self, *args, **options):
        with open(options['csv_file'], 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                Tourmodel.objects.get_or_create(
                    location=row[0], 
                    location_code=row[1], 
                    positive=row[2], 
                    negative=row[3], 
                    image=row[4],  
                    tour_loc_1=row[5],
                    tour_loc_2=row[6],
                    tour_loc_3=row[7],

                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))


