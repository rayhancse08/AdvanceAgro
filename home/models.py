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
        verbose_name_plural="Slide Photos"


class About(models.Model):
    about= models.TextField("About Advance Agro",help_text="About Page Contents")
    def __str__(self):
        return self.about
    class Meta:
        verbose_name_plural="About Page Contents"


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
    def __str__(self):
        return self.formula
    class Meta:
        verbose_name_plural = "Rationing Formula"


class Cow(models.Model):
    cow_no = models.CharField("গরু নং ",max_length=100,null=True,unique=True)
    def __str__(self):
        return self.cow_no

class Disease(models.Model):
    name=models.CharField("টিকার নাম", max_length=100,null=True)
    def __str__(self):
        return self.name


class VaccineSchedule(models.Model):
    vaccinename = models.CharField("টিকার নাম", max_length=100)
    vaccinedose = models.CharField("প্রয়োগ মাত্রা", max_length=100)
    vaccineInterval = models.CharField("কতদিন পর পর", max_length=100)
    eligableAge = models.CharField("কোন বয়সে", max_length=100)
    pushingPosition = models.CharField("প্রয়ােগ স্থান", max_length=100)
    preserveTemp = models.CharField("সংরক্ষণ তাপমাত্রা", max_length=100)
    def __str__(self):
        return self.vaccinename




class DiseaseManagement(models.Model):
    cow =models.ForeignKey(Cow,on_delete=models.CASCADE,verbose_name="গরু নং",null=True,blank=True)
    disease=models.ForeignKey(Disease,on_delete=models.CASCADE,verbose_name="টিকার নাম",null=True,blank=True)
    ScheduleTime = models.DateField("টিকা প্রদাণের সময়", null=True)
    NextScheduleTime = models.DateField("পরবর্তী প্রদাণের তারিখ", null=True)
    def __str__(self):
        return str(self.ScheduleTime)
    class Meta:
        ordering = ['ScheduleTime']
        verbose_name_plural="Vaacine Records"



class BioSecurity(models.Model):
    bioSecurity = models.TextField()
    def __str__(self):
        return self.bioSecurity
    class Meta:
        verbose_name_plural="Bioseceurty Page Contents"

class Grass(models.Model):
    grassName=models.CharField("ঘাস পরিচিতি", max_length=100)
    suitableField=models.TextField("উপযোগী জমি")
    plantationTime=models.TextField("চাষের সময়")
    plantationProcedure=models.TextField("চাষের পদ্ধতিঃ")
    fertilizer=models.TextField("সার")
    waterIrrigation=models.TextField("পানি সেচ")
    grassCollection=models.TextField("ঘাস সংগ্রহ")
    problemAndCaution=models.TextField("সমস্যা ও সতর্কতা")
    def __str__(self):
        return self.grassName
    class Meta:
        verbose_name_plural="Grass Informations"


class Medicine(models.Model):
    diseaseName=models.CharField("Disease Name", max_length=100)
    medicineName=models.TextField("Medicine Name")
    def __str__(self):
        return self.diseaseName
    class Meta:
        verbose_name_plural="Medicine Informations"

class DailyRoutine(models.Model):
    dailyRoutine=models.TextField("Daily Routine")
    def __str__(self):
        return self.dailyRoutine
    class Meta:
        verbose_name_plural="Daily Routine Page Contents"

class Document(models.Model):
    documents=models.TextField("Documents")
    def __str__(self):
        return self.documents
    class Meta:
        verbose_name_plural="Sticky Note Page Contents"


class Breeding(models.Model):
    cow=models.ForeignKey(Cow,on_delete=models.CASCADE,verbose_name="গরু নং",null=True,blank=True)
    breeding_info=models.TextField("প্রজণন সংক্রান্ত তথ্য")
    breeding_date=models.DateField("বীজ দেওয়ার তারিখ",null=True)
    expacted_delivery_date=models.DateField("বাচ্চা প্রসবের সম্ভাব্য তারিখ", null=True)
    delivery_date=models.DateField("বাচ্চা প্রসবের তারিখ", null=True)

    def __str__(self):
        return str(self.breeding_date)
    class Meta:
        ordering = ['breeding_date']
        verbose_name_plural="Breeding Records"


class CowDetail(models.Model):
       cow_status=(
        ('Milking', 'Milking'),
        ('Dry Preiod', 'Dry Preiod'),
        ('Calf', 'Calf'),
        ('Fattening','Fattening')
    )
       cow=models.OneToOneField(Cow,on_delete=models.CASCADE,verbose_name="গরু নং",null=True,blank=True,unique=True)
       age=models.FloatField("গরুর বয়স",default=0)
       weight=models.FloatField("গরুর ওজন",default=0)
       number_of_teeth=models.IntegerField("দাঁত সংখ্যা",default=0)
       status=models.CharField(max_length=10, choices=cow_status,verbose_name="গরুর ধরন")
       collected_time_info=models.TextField("সংগ্রহকালীন তথ্য",null=True)
       class Meta:
           verbose_name_plural="Cow Records"

class MilkManagement(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE, verbose_name="গরু নং", null=True, blank=True)
    date=models.DateField("তারিখ", null=True)
    milk_quantity=models.FloatField("দুধের পরিমান",default=0)
    milk_price=models.FloatField("দুধের দাম",default=0)
    def __str__(self):
        return str(self.date)
    class Meta:
        ordering = ['date']
        verbose_name_plural="Milk Records"


class FoodManagement(models.Model):
    cow=models.ForeignKey(Cow,on_delete=models.CASCADE,verbose_name="গরু নং",null=True,blank=True)
    date=models.DateField("তারিখ", null=True)
    mixed_food=models.FloatField("দানাদার খাদ্য(কে.জি)",default=0)
    mixed_food_price=models.FloatField("দানাদার দাম",default=0)
    grass=models.FloatField("ঘাস(কে.জি)",default=0)
    grass_cost=models.FloatField("ঘাসের দাম",default=0)
    khor=models.FloatField("খড়(কে.জি)",default=0)
    khor_cost=models.FloatField("খড়ের দাম",default=0)
    water=models.FloatField("পানি(লিটার)",default=0)
    def __str__(self):
        return str(self.date)
    class Meta:
        ordering = ['date']
        verbose_name_plural="Food Records"

class File(models.Model):
    name = models.CharField("Doc Name", max_length=200, help_text="Enter File Name")
    file = models.FileField(default=False, help_text="Upload File")
    upload_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['upload_time']
        verbose_name_plural="Upload File"

class Costing(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE, verbose_name="গরু নং", null=True, blank=True)
    date = models.DateField("তারিখ", null=True)
    costing_amount=models.FloatField("খরচের পরিমান",default=0)
    costing_description=models.CharField("খরচের বর্ণনা", max_length=200)

class Earning(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE, verbose_name="গরু নং", null=True, blank=True)
    date = models.DateField("তারিখ", null=True)
    earning_amount = models.FloatField("আয়ের পরিমান", default=0)
    earning_description = models.CharField("আয়ের বর্ণনা", max_length=200)
