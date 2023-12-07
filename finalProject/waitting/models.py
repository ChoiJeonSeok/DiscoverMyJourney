from django.db import models

class Place(models.Model):
    location = models.CharField(max_length=200)
    gender = models.CharField(max_length=1)
    age = models.CharField(max_length=1)
    family = models.BooleanField(default=False)
    rating = models.FloatField()

    def __str__(self):
        return f"{self.location}, {self.gender}, {self.age}, {self.family}, {self.rating}"

class Area(models.Model):
    area = models.CharField(max_length=200)  # 지역 이름
    average_vector = models.TextField()  # 평균 벡터, 문자열로 저장하고 필요할 때 리스트로 변환
    cluster = models.IntegerField()  # 클러스터 번호

    def __str__(self):
        return f"{self.area}, {self.average_vector}, {self.cluster}"
