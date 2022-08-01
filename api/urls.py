from django.urls import path
from . import views

urlpatterns = [
        path("code/<str:code>/", views.title_by_code, name="title_by_code"),
        path("title/<str:title>/", views.title_by_title, name="title_by_title"),
        path("stats/", views.stats, name="stats"),
        path("field_update/", views.field_update, name="field_update"),
        path("status_update/", views.status_update, name="status_update"),
        path("field_data/", views.field_data, name="field_data"),
        path("zakryto/", views.zakryto, name="api_zakryto")
]
