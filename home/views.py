from django.shortcuts import render
from .models import Produkt

def index(request):
    produkty = Produkt.objects.order_by("id")
    return render(request, "home/index.html", { "produkty": produkty })

def produkt(request, produkt_id):
    produkt = Produkt.objects.get(pk=produkt_id)

    return render(request, "home/produkt.html", { "produkt": produkt })
