from django.shortcuts import render, HttpResponse, redirect
from .models import Photo
from .models import CowFood
from .forms import *
from .models import *
import time;
import datetime
from django.db.models import Count, Avg


def home(request):
    today = datetime.datetime.now().date()
    photo = Photo.objects.all()
    content = {"photo": photo}
    return render(request, 'home.html', content)
    # return redirect("https://www.djangoproject.com")
    # return render(request,'home.html')


def about(request):
    about=About.objects.all()
    return render(request, 'about.html',{"about":about})


def food(request):
    objects1 = CowFood.objects.all()

    return render(request, 'food.html', {"res": objects1})


def mixed_food(request):
    objectsMixedFood = CowFood.objects.all()
    objectFormula1 = CowFood.objects.filter()[:1].get()
    objectFormula2 = CowFood.objects.filter()[1:2].get()
    objectFormula3 = CowFood.objects.filter()[2:3].get()
    objectFormula4 = CowFood.objects.filter()[3:4].get()
    return render(request, 'mixed_food.html',
                  {"formula1": objectFormula1, "formula2": objectFormula2, "formula3": objectFormula3,
                   "formula4": objectFormula4})
    # return render(request, 'mixed_food.html')


def totalMixedFood(request):
    objectsMixedFood = CowFood.objects.all()
    return render(request, 'totalMixedFood.html', {"res": objectsMixedFood})


def bodyWeightCal(request):
    return render(request, 'bodyWeightCal.html')

def bodyWeightCalResult(request):
    if request.method == 'POST':
        bodyLength=request.POST['bodyLength']
        bodyGrith=request.POST['bodyGrith']
        bodyWeight=float(bodyLength)*float(bodyGrith)*float(bodyGrith)/660
        bodyWeightRound=round(bodyWeight,2)

        return render(request,'bodyWeightCalResult.html',{"bodyLength":bodyLength,"bodyGrith":bodyGrith,"bodyWeight":bodyWeightRound})

def dmiFood(request):
    return render(request, 'dmiFood.html')


def rationingMixedFood(milkQuantity):
    minimuMixFood = 3
    milkQuantity = int(milkQuantity)
    if milkQuantity > 3:
        mixedFood = (milkQuantity - 3) / 3 + minimuMixFood
        return mixedFood
    else:
        return minimuMixFood


def dmiFoodCal(request):
    if request.method == 'POST':

        milkQuantity = request.POST["milkQuantity"]
        bodyWeight = request.POST["bodyWeight"]
        milkStatus = request.POST["optradio"]

        if milkStatus == "highMilk":
            totalDMIFoodStart = int(bodyWeight) * 5 / 100
            totalDMIFoodEnd = int(bodyWeight) * 6 / 100
        if milkStatus == "goodMilk":
            totalDMIFoodStart = int(bodyWeight) * 4 / 100
            totalDMIFoodEnd = int(bodyWeight) * 3.5 / 100

        if milkStatus == "dryPreiod":
            totalDMIFoodStart = int(bodyWeight) * 2.5 / 100
            totalDMIFoodEnd = int(bodyWeight) * 2 / 100
        # print(milkQuantity)
        return render(request, 'dmiFoodCal.html',
                      {"milkQunatity": milkQuantity, "bodyWeight": bodyWeight, "milkStatus": milkStatus,
                       "DMIStart": totalDMIFoodStart, "DMIEnd": totalDMIFoodEnd,
                       "mixedFood": rationingMixedFood(milkQuantity)})
    # return render(request, 'dmiFoodCal.html')
    # form = DMIFoodCal(request.post)
    # if form.is_valid():

    # milkQuantity = form.cleaned_data['milkQuantity']
    # bodyWeight=form.cleaned_data['bodyWeight']
    # milkStatus=form.cleaned_data['milkStatus']


def signAndSymptom(request):
    return render(request, 'signAndSymptom.html')


def vaccineSchedule(request):
    vaccine = VaccineSchedule.objects.all()
    return render(request, 'vaccineSchedule.html', {"vaccine": vaccine})


def bioSecurity(request):
    bioSecurity = BioSecurity.objects.all()
    return render(request, 'bioSecurity.html', {"bioSecurity": bioSecurity})


def diseaseManagement(request):
    diseaseManagement=DiseaseManagement.objects.all()
    #vaccine=FMDSchedule.objects.order_by("disease_id")[::0]
    lastvaccine=FMDSchedule.objects.last()
    vaccine=FMDSchedule.objects.all()
    #diseaseManagement = DiseaseManagement.objects.order_by('cowNo').distinct()
    # cowNo=DiseaseManagement.objects.values('cowNo').distinct()
    # diseaseManagement = DiseaseManagement.objects.all().values('cowNo').order_by('cowNo').annotate(count=Count('cowNo'))
    # diseaseManagement = DiseaseManagement.objects.values('cowNo').annotate(count=Count('cowNo')).order_by()
    return render(request, 'diseaseManagement.html', {"disease": diseaseManagement,"lastvaccine":lastvaccine,"vaccine":vaccine})


def dailyRoutine(request):
    dailyRoutineObject=DailyRoutine.objects.all()
    return render(request, 'dailyRoutine.html',{"dailyRoutine":dailyRoutineObject})


def grass(request):
    grassObject=Grass.objects.all()

    return render(request,'grass.html',{"grass":grassObject})

def medicine(request):
    medicineObject=Medicine.objects.all()
    return render(request,'medicine.html',{"medicine":medicineObject})

def documents(request):
    leftcol=Document.objects.all()[::2]
    rightcol=Document.objects.all()[1::2]
    return render(request,'documents.html',{"leftcol":leftcol,"rightcol":rightcol})

















