from django.db import models


# Create your models here.
class Sisul(models.Model):
    id = models.BigAutoField(primary_key=True,)
    name = models.CharField(max_length=30) #시설명
    longitude = models.FloatField() #경도
    latitude = models.FloatField() #위도
    zipcode = models.CharField(max_length=5) #우편번호
    #safety = models.CharField(max_length=4) # 안전/위험시설 구분(대분류)
    category = models.CharField(max_length=30) # 시설종류(중분류)
    info = models.CharField(max_length=30) # 시설정보(소분류)
