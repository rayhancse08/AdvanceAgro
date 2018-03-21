from django.db import models

update_time = models.DateTimeField(null=True)


# Create your models here.
class Photo(models.Model):
    titles = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False, width_field='width', height_field='height')
    upload_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.titles

    class Meta:
        ordering = ['-upload_time']


class About(models.Model):
    about= models.TextField("About Advance Agro")

class CowFood(models.Model):
    formula = models.CharField("মিশ্রণ তালিকা", max_length=100)
    cornMix = models.IntegerField("ভুট্টা ভাংগা", default=0)
    wheatMix = models.IntegerField("গম ভাংগা", default=0)
    wheatBhushi = models.IntegerField("গমের ভুষি", default=0)
    riceBran = models.IntegerField("রাইস ব্রান", default=0)
    dalMix = models.IntegerField("ডাল ভাংগা", default=0)
    dalBhushi = models.IntegerField("ডাল ভুষি", default=0)
    khoil = models.IntegerField("খৈল", default=0)
    limestonDCP = models.IntegerField("লাইমস্টোন/ডি,সি,পি", default=0)
    soda = models.IntegerField("সোডা", default=0)
    salt = models.IntegerField("লবণ", default=0)
    vitamin = models.IntegerField("ভিটামিন প্রিমিক্স", default=0)


class Cow_Detail(models.Model):
    cow_no = models.IntegerField(default=0)
    cow_weight = models.IntegerField(default=0)
    cow_milk = models.IntegerField(default=0)
    cow_status = models.CharField(max_length=200)


class VaccineSchedule(models.Model):
    vaccinename = models.CharField("টিকার নাম", max_length=100)
    vaccinedose = models.CharField("প্রয়োগ মাত্রা", max_length=100)
    vaccineInterval = models.CharField("কতদিন পর পর", max_length=100)
    eligableAge = models.CharField("কোন বয়সে", max_length=100)
    pushingPosition = models.CharField("প্রয়ােগ স্থান", max_length=100)
    preserveTemp = models.CharField("সংরক্ষণ তাপমাত্রা", max_length=100)


class DiseaseManagement(models.Model):
    cowNo = models.CharField("গরু নং ", max_length=100)
    ScheduleTime = models.DateField("ক্ষুরারােগ টিকা প্রদাণের সময়", null=True)

class FMDSchedule(models.Model):
    disease = models.ForeignKey(DiseaseManagement, related_name='FMD', on_delete=models.CASCADE,verbose_name="গরু নং")
    NextScheduleTime = models.DateField("পরবর্তী প্রদাণের তারিখ", null=True)


class BioSecurity(models.Model):
    bioSecurity = models.TextField()

class Grass(models.Model):
    grassName=models.CharField("ঘাস পরিচিতি", max_length=100)
    suitableField=models.TextField("উপযোগী জমি")
    plantationTime=models.TextField("চাষের সময়")
    plantationProcedure=models.TextField("চাষের পদ্ধতিঃ")
    fertilizer=models.TextField("সার")
    waterIrrigation=models.TextField("পানি সেচ")
    grassCollection=models.TextField("ঘাস সংগ্রহ")
    problemAndCaution=models.TextField("সমস্যা ও সতর্কতা")

class Medicine(models.Model):
    diseaseName=models.CharField("Disease Name", max_length=100)
    medicineName=models.TextField("Medicine Name")

class DailyRoutine(models.Model):
    dailyRoutine=models.TextField("Daily Routine")

class Document(models.Model):
    documents=models.TextField("Documents")