# load_data_from_csv.py
from django.core.management.base import BaseCommand, CommandError
from waitting.models import Place
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
                Place.objects.get_or_create(
                    location=row[0],  # 시군구
                    gender=row[5],  # 성별
                    age=row[6],  # 연령대
                    family=row[1],  # 동반자유형
                    rating=float(row[7])  # 평점
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))


