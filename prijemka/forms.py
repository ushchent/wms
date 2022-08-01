from django.forms import ModelForm
from prijemka.models import Artikul, Truck
from django import forms

class ArtikulForm(ModelForm):
    class Meta:
        model = Artikul
        fields = ["code", "in_field", "status"]

class TruckForm(ModelForm):
    class Meta:
        model = Truck
        fields = []

class FileUploadForm(ModelForm):
    class Meta:
        model = Truck
        fields = ["truck_info", "date", "data"]
        labels = {
                "truck_info": "Номер приходного счета",
                "date": "Дата прихода машины",
                "data": "Список товаров"

                }

