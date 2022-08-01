from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("prijemka/", include("prijemka.urls")),
    path("api/", include("api.urls")),
    path("otgruzka/", include("otgruzka.urls"))
]
