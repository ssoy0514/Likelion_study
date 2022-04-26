import csv
import os
import django

# 환경 변수 설정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "search.settings")
django.setup()

# mainApp 폴더에 존재하는 models.py에서 Building 모델을 불러온다
from searchapp.models import Building

with open('C:/Users/badr1/Desktop/LikeLion Study/study/search/building_data.csv', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Building.objects.get_or_create(
            name = row[0],
            address = row[1],
            latitude = row[2],
            longitude = row[3]
        )