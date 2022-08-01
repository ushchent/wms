from django.urls import path, include
from . import views

app_name = "prijemka"

urlpatterns = [
    path("", views.index, name="home"),
    path("upload/", views.data_upload, name="upload"), 
    path("stats/", views.stats, name="stats"),
    path("field/", views.field, name="field"),
    path("zakryto/", views.zakryto, name="zakryto"),
    path("process/<str:truck_info>/", views.process, name="process")

]
