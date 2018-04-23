from django.contrib import admin
from .models import Photo,About,CowFood,VaccineSchedule,BioSecurity,Cow,Disease,DiseaseManagement,DailyRoutine,Document,Medicine,Grass,Breeding,CowDetail,MilkManagement,FoodManagement,File



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


class CowAdmin(admin.ModelAdmin):
    list_display=['cow_no']
    class Meta:
        model=Cow

class DiseaseAdmin(admin.ModelAdmin):
    list_display=['name']
    class Meta:
        model=Disease

class VaccineScheduleAdmin(admin.ModelAdmin):
    list_display =['vaccinename','vaccinedose','vaccineInterval','eligableAge','pushingPosition','preserveTemp']
    class Meta:
        model=VaccineSchedule

class BioSecurityAdmin(admin.ModelAdmin):
    list_display=['bioSecurity']
    class Meta:
        model=BioSecurity



class DiseaseManagementAdmin(admin.ModelAdmin):
    list_display = ['cow','disease','ScheduleTime','NextScheduleTime']

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

class BreedingAdmin(admin.ModelAdmin):
    list_display=['cow','breeding_info','breeding_date','expacted_delivery_date','delivery_date']
    class Meta:
        model=Breeding


class CowDetailAdmin(admin.ModelAdmin):
    list_display=['cow','age','weight','number_of_teeth','status','collected_time_info']
    class Meta:
        model=CowDetail

class MilkManagementAdmin(admin.ModelAdmin):
    list_display=['cow','date','milk_quantity']
    class Meta:
        model=MilkManagement


class FoodManagementAdmin(admin.ModelAdmin):
    list_display=['cow','date','mixed_food','grass','khor','water']
    class Meta:
        model=FoodManagement

class FileAdmin(admin.ModelAdmin):
    list_display=['name','file']
    class Meta:
        model=File


admin.site.register(Cow,CowAdmin)
admin.site.register(CowFood,CowFoodAdmin)
admin.site.register(Photo,PhotoAdmin)
admin.site.register(VaccineSchedule,VaccineScheduleAdmin)
admin.site.register(BioSecurity,BioSecurityAdmin)
admin.site.register(DiseaseManagement,DiseaseManagementAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Grass,GrassAdmin)
admin.site.register(Medicine,MedicineAdmin)
admin.site.register(DailyRoutine,DailyRoutineAdmin)
admin.site.register(Document,DocumentAdmin)
admin.site.register(Disease,DiseaseAdmin)
admin.site.register(Breeding,BreedingAdmin)
admin.site.register(CowDetail,CowDetailAdmin)
admin.site.register(MilkManagement,MilkManagementAdmin)
admin.site.register(FoodManagement,FoodManagementAdmin)
admin.site.register(File,FileAdmin)












# Register your models here.
