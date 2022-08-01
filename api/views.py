from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .serializers import ArtikulSerializer, FieldSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from prijemka.models import Artikul
from django.db.models import Sum, Count
from django.core import serializers

@api_view(["GET"])
def overview(request):
    api_urls = {
        "Artikul": "/code/"        
    }
    return Response(api_urls)

@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def stats(request):
    artikul_count = Artikul.objects.all().count()
    total_boxes = Artikul.objects.aggregate(Sum("boxes"))["boxes__sum"]

    gotovo = Artikul.objects.filter(status=True).count() /\
                Artikul.objects.all().count() * 100

    artikul_by_sector = Artikul.objects.values("sector")\
                        .annotate(sector_count=Count("sector"))\
                        .order_by("sector_count")

    boxes_by_sector = Artikul.objects.values("sector")\
        .annotate(sector_sum=Sum("boxes"))\
        .order_by("sector_sum")
    boxes_by_sector_dict = [ { "sector": datum["sector"], "boxes":
        int(datum["sector_sum"]) } for datum in boxes_by_sector ]
    
    artikul_by_sector_dict = [ { "sector": datum["sector"], "count":
        int(datum["sector_count"]) } for datum in artikul_by_sector ]
    result_data = {"by_sector": boxes_by_sector_dict, "by_artikul":
            artikul_by_sector_dict, "total_artikul":
            int(artikul_count), "total_boxes": int(total_boxes), "gotovo":
            int(gotovo)}

    #serializer = ArtikulSerializer(boxes_by_sector, many=True)
    return JsonResponse(result_data, safe=False)
    
    
    # return HttpResponse("Всего артикулов в машине: {}<br>Всего грузовых мест:\
   #         {}".format(artikul_count, int(total_boxes)))

@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def title_by_code(request, code):
    items = Artikul.objects.filter(code__startswith=code)
    serializer = ArtikulSerializer(items, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def title_by_title(request, title):
    items = Artikul.objects.filter(title__contains=title[1:])
    serializer = ArtikulSerializer(items, many=True)
    return Response(serializer.data)
#JsonResponse({"code": code, "title": item.title, "v_pole":
        #item.in_field, "korobok": item.boxes, "status": item.status })

@api_view(["GET"])
#@authentication_classes([SessionAuthentication, BasicAuthentication])
#@permission_classes([IsAuthenticated])
def field_data(request):
    data_in_field = Artikul.objects.filter(in_field__gt=0, status=False)
    serializer = FieldSerializer(data_in_field, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(["POST"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def field_update(request):
    print(request.data)
    target = Artikul.objects.filter(code=request.data["code"])
    print(target)
    target.update(in_field=request.data["in_field"])
    return HttpResponse("Ok")

@api_view(["POST"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def status_update(request):
    print(request.data)
    target = Artikul.objects.filter(code=request.data["code"])
    print(request.data["status"])
    target.update(status=request.data["status"])
    return HttpResponse("Ok")

@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def zakryto(request):
    data_zakryty = Artikul.objects.filter(status=True)
    serializer = ArtikulSerializer(data_zakryty, many=True)
    return JsonResponse(serializer.data, safe=False)
