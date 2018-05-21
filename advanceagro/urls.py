"""advanceagro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('mixed_food/',mixed_food,name='mixed_food'),
    path('totalMixedFood/',totalMixedFood, name='totalMixedFood'),
    path('bodyWeightCal/',bodyWeightCal, name='bodyWeightCal'),
    path('bodyWeightCalResult/', bodyWeightCalResult, name='bodyWeightCalResult'),
    path('dmiFood/',dmiFood, name='dmiFood'),
    path('dmiFoodCal/',dmiFoodCal, name='dmiFoodCal'),
    path('signAndSymptom/',signAndSymptom, name='signAndSymptom'),
    path('vaccineSchedule/',vaccineSchedule, name='vaccineSchedule'),
    path('bioSecurity/',bioSecurity, name='bioSecurity'),
    path('diseaseManagement/',diseaseManagement, name='diseaseManagement'),
    path('searchDiseaseManagement/',searchDiseaseManagement, name='searchDiseaseManagement'),
    path('dailyRoutine/',dailyRoutine,name='dailyRoutine'),
    path('grass/',grass,name='grass'),
    path('medicine/',medicine,name='medicine'),
    path('documents/',documents,name='documents'),
    path('breeding/',breeding,name='breeding'),
    path('breedingHistory/',breedingHistory,name='breedingHistory'),
    path('cowsRecord/',cowsRecord,name='cowsRecord'),
    path('searchCowsRecord/',searchCowsRecord,name='searchCowsRecord'),
    path('milkManagement/',milkManagement,name='milkManagement'),
    path('searchMilkManagement/',searchMilkManagement,name='searchMilkManagement'),
    path('foodManagement/',foodManagement,name='foodManagement'),
    path('searchFoodManagement/',searchFoodManagement,name='searchFoodManagement'),
    path('file/',file,name='file'),
    path('profitLoss/',profitLoss,name='profitLoss'),
    path('getProfitLoss/',getProfitLoss,name='getProfitLoss/'),
    path('detailProfitLoss/',detailProfitLoss,name='detailProfitLoss')

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

