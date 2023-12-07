# load_data_from_csv.py
from django.core.management.base import BaseCommand, CommandError
from waitting.models import Area
import csv

class Command(BaseCommand):
    help = 'Load data from CSV file into Database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The csv file to load data from')

    def handle(self, *args, **options):
        with open(options['csv_file'], 'r', encoding='cp949') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                Area.objects.get_or_create(
                    area=row[0],  
                    average_vector=row[1],  
                    cluster=row[2],  

                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))


