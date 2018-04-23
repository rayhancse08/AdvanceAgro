from django import forms
from django.forms import widgets
class Mixed_Food(forms.Form):
    mixed_food_amount=forms.CharField(max_length = 100)
#class DMIFoodCal(forms.Form):
    #milkQuantity=forms.NumberInput()
    #bodyWeight=forms.NumberInput()
    #milkStatus=forms.RadioSelect()
