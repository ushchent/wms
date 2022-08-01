from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

# Всегда использовать app_name. В таком случае можно указывать одинаковые name
# для маршрутов на уровне приложения, а на уровне проекта различать их через
# синтаксис app_name:name.

app_name = "homepage"

urlpatterns = [
    path("", views.index, name="home"),
    path("produkt/<int:produkt_id>/", views.produkt, name="produkt"),
    path("login/", LoginView.as_view(template_name="home/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
