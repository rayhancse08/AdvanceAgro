from django.shortcuts import render,redirect
from .models import Photo,About,CowFood,VaccineSchedule,BioSecurity,Cow,Disease,DiseaseManagement,DailyRoutine,Document,Medicine,Grass,Breeding,CowDetail,MilkManagement,FoodManagement,File,Costing,Earning
import datetime
from django.db.models import Sum,Avg,F,Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

        return render(request,'bodyWeightCal.html',{"bodyLength":bodyLength,"bodyGrith":bodyGrith,"bodyWeight":bodyWeightRound})

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

        return render(request, 'dmiFood.html',
                      {"milkQunatity": milkQuantity, "bodyWeight": bodyWeight, "milkStatus": milkStatus,
                       "DMIStart": totalDMIFoodStart, "DMIEnd": totalDMIFoodEnd,
                       "mixedFood": round(rationingMixedFood(milkQuantity),2)})


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
    cow_status=exclude_selected_cows
    count_cows=[]
    for item in cow_status:
        count_cows.append(CowDetail.objects.filter(status=item['status']).count())
    zip_data=zip(count_cows,cow_status)
    return render(request,'cowsRecord.html',{"exclude_selected_cows":exclude_selected_cows,"zip_data":zip_data})

def searchCowsRecord(request):
    cows = CowDetail.objects.order_by().values('status').distinct()
    count_cows = []
    for item in cows:
        count_cows.append(CowDetail.objects.filter(status=item['status']).count())
    zip_data = zip(count_cows, cows)
    if request.method=="GET":
         select_cow_status=request.GET['select_cow_status']
         exclude_selected_cows = CowDetail.objects.exclude(status=select_cow_status).order_by().values(
             'status').distinct()
         selected_cows=CowDetail.objects.filter(status=select_cow_status)
         total_cows =selected_cows.count()

         if selected_cows:

             page = request.GET.get('page',1)

             paginator = Paginator(selected_cows, 3)
             try:
                 pages = paginator.page(page)
             except PageNotAnInteger:
                 pages = paginator.page(1)
             except EmptyPage:
                 pages = paginator.page(paginator.num_pages)
             return render(request, 'cowsRecord.html',{"cows":cows,"selected_cows":selected_cows,"select_cow_status":select_cow_status,"exclude_selected_cows":exclude_selected_cows,"pages":pages,"page":page,"total_cows":total_cows,
                                                       "zip_data":zip_data})
         else:
             return render(request, 'cowsRecord.html', {"cows": cows,"zip_data":zip_data})



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

def profitLoss(request):
    unselected_cows = FoodManagement.objects.order_by().values('cow__cow_no').distinct()
    return render(request, 'profitLoss.html', {"unselected_cows": unselected_cows})

def getProfitLoss(request):

    if request.method == "GET":
        start_date = request.GET['startdatepicker']
        converted_start_date = datetime.datetime.strptime(start_date, "%m/%d/%Y").strftime("%Y-%m-%d")
        end_date = request.GET['enddatepicker']
        converted_end_date = datetime.datetime.strptime(end_date, "%m/%d/%Y").strftime("%Y-%m-%d")

        datewise_selected_cows = FoodManagement.objects.values(
            'cow__cow_no').filter(date__gte=converted_start_date,date__lte=converted_end_date).order_by('cow__cow_no').distinct()

        if datewise_selected_cows :
                #selected_cow = request.GET['?cow']
                cow_list = []
                total_cost_list = []
                total_earning_list = []
                profit_loss_list=[]
                for item in datewise_selected_cows :
                        cows = item['cow__cow_no']
                        cow_list.append(cows)
                        mixed_food_cost = datewise_selected_cows.filter(cow__cow_no=cows).aggregate(
                        mixed_food_cost=Sum(F('mixed_food') * F('mixed_food_price')))[
                'mixed_food_cost']
                        grass_cost = datewise_selected_cows.filter(cow__cow_no=cows).aggregate(grass_cost=Sum(F('grass') * F('grass_cost')))[
                'grass_cost']
                        khor_cost = datewise_selected_cows.filter(cow__cow_no=cows).aggregate(khor_cost=Sum(F('khor') * F('khor_cost')))[
                'khor_cost']
                        other_cost = Costing.objects.filter(cow__cow_no=cows, date__gte=converted_start_date,
                                                date__lte=converted_end_date)
                        if other_cost:
                             total_other_cost = other_cost.aggregate(total_other_cost=Sum(F('costing_amount')))[
                'total_other_cost']
                        else:
                            total_other_cost=0
                        total_cost = mixed_food_cost + grass_cost + khor_cost + total_other_cost

                        total_cost_list.append(total_cost)
                        milk_price= MilkManagement.objects.filter(cow__cow_no=cows, date__gte=converted_start_date,
                                                    date__lte=converted_end_date)

                        if milk_price:
                                total_milk_price=milk_price.aggregate(
                                total_milk_price=Sum(F('milk_quantity') * F('milk_price')))['total_milk_price']

                        else:
                            total_milk_price=0

                        other_earning = Earning.objects.filter(cow__cow_no=cows, date__gte=converted_start_date,
                                                  date__lte=converted_end_date)
                        if other_earning:

                             total_other_earning = other_earning.aggregate(total_other_earning=Sum(F('earning_amount')))[
                'total_other_earning']
                        else:
                            total_other_earning=0
                        total_earning = total_milk_price + total_other_earning
                        profit_loss=total_earning-total_cost
                        profit_loss_list.append(profit_loss)

                        total_earning_list.append(total_earning)
                page = request.GET.get('page', 1)

                paginator = Paginator(datewise_selected_cows, 1)
                try:
                    pages = paginator.page(page)
                except PageNotAnInteger:
                    pages = paginator.page(1)
                except EmptyPage:
                    pages = paginator.page(paginator.num_pages)
                return render(request, 'profitLoss.html',
                      {"start_date":start_date,"end_date":end_date,"datewise_selected_cows":datewise_selected_cows,
                        "cow_list": cow_list,
                       "total_cost_list": total_cost_list, "total_earning_list": total_earning_list,"profit_loss_list":profit_loss_list,
                       "total_earning":sum(total_earning_list),"total_cost":sum(total_cost_list),"total_profit_loss":sum(profit_loss_list),
                       "pages":pages,"page_number":range(len(pages))})


        else:

           return render(request, 'profitLoss.html',
                      {"no_data_found": "No Data Found",
                       "start_date": start_date, "end_date": end_date})


def detailProfitLoss(request):
    select_cow = request.GET['?cow']
    #report_type = request.GET['optradio']
    start_date = request.GET['startdatepicker']
    converted_start_date = datetime.datetime.strptime(start_date, "%m/%d/%Y").strftime("%Y-%m-%d")
    end_date = request.GET['enddatepicker']
    converted_end_date = datetime.datetime.strptime(end_date, "%m/%d/%Y").strftime("%Y-%m-%d")
    selected_cows = FoodManagement.objects.filter(cow__cow_no=select_cow, date__gte=converted_start_date,
                                                  date__lte=converted_end_date)
    selected_cows_milk = MilkManagement.objects.filter(cow__cow_no=select_cow, date__gte=converted_start_date,
                                                       date__lte=converted_end_date)
    unselected_cows = FoodManagement.objects.exclude(cow__cow_no=select_cow).order_by().values(
        'cow__cow_no').distinct()
    if selected_cows:
        mixed_food_cost = selected_cows.aggregate(mixed_food_cost=Sum(F('mixed_food') * F('mixed_food_price')))[
            'mixed_food_cost']
        grass_cost = selected_cows.aggregate(grass_cost=Sum(F('grass') * F('grass_cost')))['grass_cost']
        khor_cost = selected_cows.aggregate(khor_cost=Sum(F('khor') * F('khor_cost')))['khor_cost']
        other_cost = Costing.objects.filter(cow__cow_no=select_cow, date__gte=converted_start_date,
                                            date__lte=converted_end_date)
        if other_cost:
            total_other_cost = other_cost.aggregate(total_other_cost=Sum(F('costing_amount')))['total_other_cost']
        else:
            total_other_cost=0

        total_cost = mixed_food_cost + grass_cost + khor_cost + total_other_cost

        if selected_cows_milk:
            milk_price = selected_cows_milk.aggregate(milk_price=Sum(F('milk_quantity') * F('milk_price')))['milk_price']

        else:
            milk_price=0
        other_earning = Earning.objects.filter(cow__cow_no=select_cow, date__gte=converted_start_date,
                                               date__lte=converted_end_date)
        if other_earning:
            total_other_earning = other_earning.aggregate(total_other_earning=Sum(F('earning_amount')))[
            'total_other_earning']
        else:
            total_other_earning=0

        total_earning = milk_price + total_other_earning

        profit_or_loss = total_earning - total_cost
        return render(request, 'detailProfitLoss.html',
                      {"selected_cows": selected_cows, "select_cow": select_cow, "unselected_cows": unselected_cows,
                       "start_date": datetime.datetime.strptime(start_date,"%m/%d/%Y").date(), "end_date": datetime.datetime.strptime(end_date,"%m/%d/%Y").date(),
                       "selected_cows": selected_cows, "mixed_food_cost": mixed_food_cost, "grass_cost": grass_cost,
                       "khor_cost": khor_cost, "total_cost": total_cost,
                       "milk_price": milk_price, "profit_or_loss": profit_or_loss, "total_other_cost": total_other_cost,
                       "total_other_earning": total_other_earning,
                       "total_earning": total_earning})
