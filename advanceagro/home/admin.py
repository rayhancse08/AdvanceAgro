from django.contrib import admin
from .models import Photo
from .models import CowFood
from .models import Cow_Detail
from .models import*

class PhotoAdmin(admin.ModelAdmin):
    list_display=['titles','upload_time']
    class Meta:
        model=Photo


class AboutAdmin(admin.ModelAdmin):
    list_display=['about']
    class Meta:
        model=About

class CowFoodAdmin(admin.ModelAdmin):
    list_display=['formula','cornMix','wheatMix','wheatBhushi','riceBran','dalMix','dalBhushi','khoil','limestonDCP','soda','salt','vitamin']

    class Meta:
        model=CowFood

class Cow_Detail_Admin(admin.ModelAdmin):
    list_display=['cow_no','cow_weight','cow_milk','cow_status']
    class Meta:
        model=Cow_Detail


class VaccineScheduleAdmin(admin.ModelAdmin):
    list_display =['vaccinename','vaccinedose','vaccineInterval','eligableAge','pushingPosition','preserveTemp']
    class Meta:
        model=VaccineSchedule

class BioSecurityAdmin(admin.ModelAdmin):
    list_display=['bioSecurity']
    class Meta:
        model=BioSecurity

class FMDScheduleInline(admin.StackedInline):
      model =FMDSchedule

class DiseaseManagementAdmin(admin.ModelAdmin):
    list_dispay = ['cowNo', 'ScheduleTime']
    inlines = [
        FMDScheduleInline
    ]
    class Meta:
        model=DiseaseManagement

class GrassAdmin(admin.ModelAdmin):
    list_display=['grassName','suitableField','plantationTime','plantationProcedure','fertilizer','waterIrrigation','grassCollection','problemAndCaution']


class MedicineAdmin(admin.ModelAdmin):
    list_display=['diseaseName','medicineName']
    class Meta:
        model=Medicine

class DailyRoutineAdmin(admin.ModelAdmin):
    list_display=['dailyRoutine']
    class Meta:
        model=DailyRoutine

class DocumentAdmin(admin.ModelAdmin):
    list_display=['documents']
    class Meta:
        model=Document

#admin.site.register(Cow_Detail,Cow_Detail_Admin)
admin.site.register(CowFood,CowFoodAdmin)
admin.site.register(Photo,PhotoAdmin)
admin.site.register(VaccineSchedule,VaccineScheduleAdmin)
admin.site.register(BioSecurity,BioSecurityAdmin)
#admin.site.register(DiseaseManagement,DiseaseManagementAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Grass,GrassAdmin)
admin.site.register(Medicine,MedicineAdmin)
admin.site.register(DailyRoutine,DailyRoutineAdmin)
admin.site.register(Document,DocumentAdmin)







# Register your models here.
