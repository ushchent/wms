from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Truck(models.Model):
    truck_info = models.CharField(max_length=30)
    date = models.DateField(default=timezone.now)
    # Джанго хранит в БД только путь к файлу
    # Значение upload_to определяется относительно корня проекта, а не
    # приложения. Но можно указать в настройках другое значение корня в постоянной
    # MEDIA_ROOT. Теперь все значения upload_to будут относительно новой
    # MEDIA_ROOT.
    data = models.FileField(upload_to="user_data") 

    def __str__(self):
        return self.truck_info

class Artikul(models.Model):
    code = models.CharField(max_length=30)
    title = models.TextField()
    amount = models.CharField(max_length=25,null=True)
    in_field = models.IntegerField(default=0)
    tag = models.CharField(max_length=50)
    boxes = models.FloatField()
    packaging = models.CharField(max_length=50, blank=True)
    sector = models.CharField(max_length=15)
    comment = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    truck_info = models.ForeignKey(Truck, on_delete=models.CASCADE, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.title
