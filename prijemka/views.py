from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from prijemka.models import Artikul, Truck
from prijemka.forms import ArtikulForm, FileUploadForm, TruckForm
from django.http import HttpResponse, HttpResponseRedirect
import csv
from django.db.models import Count

def index(request):
    # Здесь выводить список машин от самых ранних

    truck_info_ids = [ datum.id for datum in Truck.objects.all() ]

    meta_data = { int(ids):
            Artikul.objects.filter(truck_info_id=ids,status=True).count() /
            Artikul.objects.filter(truck_info_id=ids).count() * 100 \
            for ids in truck_info_ids }


    truck_stats =  Artikul.objects.values("truck_info")\
                    .annotate(dcount=Count("truck_info"))
    trucks = Truck.objects.all()
    return_data = {"trucks": trucks, "stats": truck_stats, "meta_data": meta_data}
    return render(request, "prijemka/index.html", return_data)

def process(request, truck_info):
    return render(request, "prijemka/process.html")

def stats(request):
    return render(request, "prijemka/stats.html")

def get_sector(datum):
    sector_map = {
            "1": 1,
            "2": 3,
            "3": 2,
            "4": 2,
            "5": 1,
            "6": 2,
            "7": 3,
            "8": 1,
            "9": 3
            }

    try:
        return int(datum["sector"][-1])
    except:
        return sector_map[datum["code"][0]]


# Загрузка данных в БД

def handle_uploaded_data(request, reader):
    truck = Truck.objects.get(truck_info=request.POST["truck_info"])
    for datum in reader:
        item = Artikul(code=datum["code"],
                title=datum["title"],
                tag=datum["tag"],
                amount=datum["amount"],
                packaging=datum["packaging"],
                sector=get_sector(datum),
                boxes=datum["boxes"],
                user_id = request.user.id,
                truck_info=truck)
        item.save()


@login_required
def data_upload(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            print(request.POST["truck_info"])
            uploaded_file = request.FILES["data"]
            decoded_file = uploaded_file.read().decode("utf-8").splitlines()
            reader = csv.DictReader(decoded_file)
            form.save()
            handle_uploaded_data(request, reader)

            # instance = FileUploadForm(file_field=request.FILES["file_field"])
            # instance.save()
            print("Parsing...")
        else:
            print("Not parsing")
        return HttpResponseRedirect("/prijemka/")
    else:
        form = FileUploadForm()
        return render(request, "prijemka/upload.html", { "form": form })

def field(request):
    return render(request, "prijemka/field.html")

def zakryto(request):
    return render(request, "prijemka/zakryto.html")
