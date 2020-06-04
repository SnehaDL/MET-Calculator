from django.shortcuts import render
from .forms import BMRForm, METForm
# Create your views here.
from .models import mettable
import pdb

def bmrvalue(age ,height ,weight , gender ):
    if gender == 'm':
        BMR = 66 + (6.2 * weight ) + (12.7 * height ) - (6.76 * age ) 
    else:
        BMR = 655.1 + (4.35 * weight ) + (4.7 * height ) - (4.7 * age ) 
    return BMR 


def metvalue(act, level, hours, minutes):
    met = act * 1 * hours * minutes
    return int(met)

def BMR(request):
    if request.method == "POST":
        form = BMRForm(request.POST)
        if form.is_valid():
            age    = form.cleaned_data['age']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            gender = form.cleaned_data['gender']
            mybmr  = bmrvalue(age,float(height),float(weight),gender)
            return render (request , 'bmr_report.html', {'bmr':mybmr })
    else:
        form = BMRForm()
    return render (request , 'simple_bmr.html' , {'form': form})

def MET(request):
    if request.method == "POST":
        form = METForm(request.POST)
        if form.is_valid():
            act = form.cleaned_data['activity']
            level = form.cleaned_data['level']
            hours = form.cleaned_data['hours']
            minutes = form.cleaned_data['minutes']
            mymet  = metvalue(float(act), int(level), int(hours), int(minutes))
            return render (request , 'met_report.html', {'met':mymet })
        else:
            return render (request , 'met_report.html', {'met': ERROR })
    else:
        form = METForm()
    return render (request , 'simple_met.html' , {'form': form})

def calc(request):
    if request.method == "POST":
        form = METForm(request.POST)
        act_dict = {}
        for (key,value) in request.POST.lists():
            act_dict[key]=value
        if len(act_dict) > 1:
            count = len(act_dict['activity'])
            sumation = 0
            weeksum = 0
            for value in range(count):
                print(float(act_dict['activity'][value]), float(act_dict['level'][value]), int(act_dict['hours'][value]), int(act_dict['minutes'][value]))
                mymet = metvalue(float(act_dict['activity'][value]), float(act_dict['level'][value]), int(act_dict['hours'][value]), int(act_dict['minutes'][value]))
                print(mymet)
                sumation += mymet
                print(sumation)
                weeksum = sumation*7
                if weeksum <= 2500:
                    remmet = 2500 - weeksum
                else:
                    remmet = 0
            return render (request , 'met_report.html', {'met':float(sumation), 'weekmet':float(weeksum), 'remmet':float(remmet)})
        else:
            pdb.set_trace()
            return render (request , 'met_report.html', {'met':1 })
    allact= mettable.objects.all()    
    context= {'allactivities': allact}
    return render (request , 'met_table.html' , context)
