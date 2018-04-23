from django.shortcuts import render,redirect
from .models import Photo,About,CowFood,VaccineSchedule,BioSecurity,Cow,Disease,DiseaseManagement,DailyRoutine,Document,Medicine,Grass,Breeding,CowDetail,MilkManagement,FoodManagement,File
import datetime
from django.db.models import Sum,Avg


def home(request):
    today = datetime.datetime.now().date()
    photo = Photo.objects.all()
    content = {"photo": photo}
    return render(request, 'home.html', content)

def about(request):
    about=About.objects.all()
    return render(request, 'about.html',{"about":about})


def mixed_food(request):
    objectsMixedFood = CowFood.objects.all()
    objectFormula1 = CowFood.objects.filter()[:1].get()
    objectFormula2 = CowFood.objects.filter()[1:2].get()
    objectFormula3 = CowFood.objects.filter()[2:3].get()
    objectFormula4 = CowFood.objects.filter()[3:4].get()
    return render(request, 'mixed_food.html',
                  {"formula1": objectFormula1, "formula2": objectFormula2, "formula3": objectFormula3,
                   "formula4": objectFormula4})


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

        return render(request, 'dmiFoodCal.html',
                      {"milkQunatity": milkQuantity, "bodyWeight": bodyWeight, "milkStatus": milkStatus,
                       "DMIStart": totalDMIFoodStart, "DMIEnd": totalDMIFoodEnd,
                       "mixedFood": rationingMixedFood(milkQuantity)})


def signAndSymptom(request):
    return render(request, 'signAndSymptom.html')


def vaccineSchedule(request):
    vaccine = VaccineSchedule.objects.all()
    return render(request, 'vaccineSchedule.html', {"vaccine": vaccine})


def bioSecurity(request):
    bioSecurity = BioSecurity.objects.all()
    return render(request, 'bioSecurity.html', {"bioSecurity": bioSecurity})


def diseaseManagement(request):
    unselected_cow=DiseaseManagement.objects.order_by().values('cow__cow_no').distinct()
    disease = Disease.objects.all()
    today = datetime.date.today()
    current_month=today.strftime("%B")
    vaccine_in_current_month = DiseaseManagement.objects.filter(NextScheduleTime__year=today.year,
                                                                 NextScheduleTime__month=today.month)
    return render(request, 'diseaseManagement.html',{"unselected_cow":unselected_cow,"disease":disease,"current_month":current_month,"vaccine_in_current_month":vaccine_in_current_month,"current_year":today.year})

def searchDiseaseManagement(request):

    disease = Disease.objects.all()
    today = datetime.date.today()
    current_month = today.strftime("%B")
    vaccine_in_current_month = DiseaseManagement.objects.filter(NextScheduleTime__year=today.year,
                                                     NextScheduleTime__month=today.month)
    if request.method=="GET":
        select_cow=request.GET['select_cow']
        unselected_cow = DiseaseManagement.objects.exclude(cow__cow_no=select_cow).order_by().values('cow__cow_no').distinct()
        selected_cow = DiseaseManagement.objects.filter(cow__cow_no=select_cow).order_by().values('cow__cow_no').distinct()

        if selected_cow:
            torka=DiseaseManagement.objects.filter(cow__cow_no=select_cow,disease__name='তড়কা')
            badla=DiseaseManagement.objects.filter(cow__cow_no=select_cow,disease__name='বাদলা')
            fmd=DiseaseManagement.objects.filter(cow__cow_no=select_cow,disease__name='ক্ষুরারােগ')
            golafula=DiseaseManagement.objects.filter(cow__cow_no=select_cow,disease__name='গলাফুলা')
            krimi=DiseaseManagement.objects.filter(cow__cow_no=select_cow,disease__name='কৃমি')
            return render(request,'diseaseManagement.html',{"select_cow":select_cow,"unselected_cow": unselected_cow,"selected_cow":selected_cow,"disease":disease,"torka":torka,"badla":badla,"fmd":fmd,"golafula":golafula,"krimi":krimi,"current_month":current_month,"vaccine_in_current_month":vaccine_in_current_month,"current_year":today.year})



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

def breeding(request):
    unselected_cow =Breeding.objects.order_by().values('cow__cow_no').distinct()
    today = datetime.date.today()
    current_month = today.strftime("%B")
    breeding_in_current_month = Breeding.objects.filter(expacted_delivery_date__year=today.year,
                                            expacted_delivery_date__month=today.month)
    return render(request, 'breeding.html',
                  {"unselected_cow": unselected_cow, "current_month": current_month, "breeding_in_current_month": breeding_in_current_month, "current_year": today.year})

def breedingHistory(request):

    today = datetime.date.today()
    current_month = today.strftime("%B")
    breeding_in_current_month= Breeding.objects.filter(expacted_delivery_date__year=today.year,
                                                     expacted_delivery_date__month=today.month)


    if request.method == "GET":
        select_cow = request.GET['select_cow']
        unselected_cow = Breeding.objects.exclude(cow__cow_no=select_cow).order_by().values('cow__cow_no').distinct()
        selected_cow = Breeding.objects.filter(cow__cow_no=select_cow)

        if selected_cow:

             return render(request, 'breeding.html',
                          {"select_cow": select_cow, "unselected_cow": unselected_cow, "selected_cow": selected_cow,
                           "current_month": current_month, "current_month": current_month, "current_year": today.year,"selected_cow":selected_cow,"breeding_in_current_month":breeding_in_current_month})





def cowsRecord(request):
    exclude_selected_cows=CowDetail.objects.order_by().values('status').distinct()
    return render(request,'cowsRecord.html',{"exclude_selected_cows":exclude_selected_cows})

def searchCowsRecord(request):
    cows = CowDetail.objects.order_by().values('status').distinct()
    if request.method=="GET":
         select_cow_status=request.GET['select_cow_status']
         exclude_selected_cows = CowDetail.objects.exclude(status=select_cow_status).order_by().values(
             'status').distinct()
         selected_cows=CowDetail.objects.filter(status=select_cow_status)

         if selected_cows:
             return render(request, 'cowsRecord.html',{"cows":cows,"selected_cows":selected_cows,"select_cow_status":select_cow_status,"exclude_selected_cows":exclude_selected_cows})
         else:
             return render(request, 'cowsRecord.html', {"cows": cows})



def milkManagement(request):
    unselected_cows = MilkManagement.objects.order_by().values('cow__cow_no').distinct()
    return  render (request,'milkManagement.html',{"unselected_cows":unselected_cows})

def searchMilkManagement(request):

    if request.method == "GET":
        select_cow = request.GET['select_cow']
        start_date=request.GET['startdatepicker']
        converted_start_date=datetime.datetime.strptime(start_date,"%m/%d/%Y").strftime("%Y-%m-%d")
        end_date=request.GET['enddatepicker']
        converted_end_date=datetime.datetime.strptime(end_date,"%m/%d/%Y").strftime("%Y-%m-%d")
        selected_cows = MilkManagement.objects.filter(cow__cow_no=select_cow,date__gte=converted_start_date,date__lte=converted_end_date)
        unselected_cows = MilkManagement.objects.exclude(cow__cow_no=select_cow).order_by().values(
            'cow__cow_no').distinct()
        if selected_cows:
            total_milk_quantity=selected_cows.aggregate(Sum('milk_quantity'))
            return render(request, 'milkManagement.html',{"select_cow":select_cow,"selected_cows":selected_cows,"unselected_cows":unselected_cows,"start_date":start_date,"end_date":end_date,"count":selected_cows.count(),"total":total_milk_quantity})

        else:

            return render(request, 'milkManagement.html', {"unselected_cows": unselected_cows,"no_data_found":"No Data Found","select_cow":select_cow,"start_date":start_date,"end_date":end_date})

def foodManagement(request):
    unselected_cows = FoodManagement.objects.order_by().values('cow__cow_no').distinct()
    return render(request, 'foodManagement.html', {"unselected_cows": unselected_cows})

def searchFoodManagement(request):
    if request.method == "GET":
        select_cow = request.GET['select_cow']
        start_date=request.GET['startdatepicker']
        converted_start_date=datetime.datetime.strptime(start_date,"%m/%d/%Y").strftime("%Y-%m-%d")
        end_date=request.GET['enddatepicker']
        converted_end_date=datetime.datetime.strptime(end_date,"%m/%d/%Y").strftime("%Y-%m-%d")
        selected_cows = FoodManagement.objects.filter(cow__cow_no=select_cow,date__gte=converted_start_date,date__lte=converted_end_date)
        unselected_cows = FoodManagement.objects.exclude(cow__cow_no=select_cow).order_by().values(
            'cow__cow_no').distinct()
        if selected_cows:
            total_mixed_food=selected_cows.aggregate(Sum('mixed_food'))
            total_grass=selected_cows.aggregate(Sum('grass'))
            total_khor=selected_cows.aggregate(Sum('khor'))
            total_water=selected_cows.aggregate(Sum('water'))
            return render(request, 'foodManagement.html',{"select_cow":select_cow,"selected_cows":selected_cows,"unselected_cows":unselected_cows,"start_date":start_date,"end_date":end_date,"count":selected_cows.count(),"total_mixed_food":total_mixed_food,"total_grass": total_grass,"total_khor":total_khor,"total_water":total_water})

        else:

            return render(request, 'foodManagement.html', {"unselected_cows": unselected_cows,"no_data_found":"No Data Found","select_cow":select_cow,"start_date":start_date,"end_date":end_date})


def file(request):
    file=File.objects.all()
    return render(request,'file.html',{"file":file})








