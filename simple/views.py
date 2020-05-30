from django.shortcuts import render
from .forms import BMRForm
# Create your views here.


def bmrvalue(age ,height ,weight , gender ):
    if gender == 'm':
        BMR = 66 + (6.2 * weight ) + (12.7 * height ) - (6.76 * age ) 
    else:
        BMR = 655.1 + (4.35 * weight ) + (4.7 * height ) - (4.7 * age ) 
    return BMR 


def metvalue(act, level, hours, minutes):
    met = act * hours * minutes
    return met

def BMR(request):
    if request.method == "POST":
        form = BMRForm(request.POST)
        if form.is_valid():
            age    = form.cleaned_data['age']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            gender = form.cleaned_data['gender']
            mybmr  = bmrvalue(age,height,weight,gender)
            return render (request , 'bmr_report.html', {'bmr':mybmr })
    else:
        form = BMRForm()
    return render (request , 'bmr.html' , {'form': form})

def MET(request):
    if request.method == "POST":
        form = METForm(request.POST)
        if form.is_valid():
            act = form.cleaned_data['activity']
            level = form.cleaned_data['level']
            hours = form.cleaned_data['hours']
            minutes = form.cleaned_data['minutes']
            mybmr  = metvalue(act, level, hours, minutes)
            return render (request , 'met_report.html', {'bmr':mybmr })
    else:
        form = METForm()
    return render (request , 'met.html' , {'form': form})
