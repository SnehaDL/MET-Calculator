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
    if hours == 0:
        met = act * minutes
    elif minutes == 0:
        met = act * hours
    else:
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
            mymet  = metvalue(float(act), float(level), int(hours), int(minutes))
            return render (request , 'met_report1.html', {'met':mymet })
        else:
            return render (request , 'met_report1.html', {'met': ERROR })
    else:
        form = METForm()
    return render (request , 'simple_met.html' , {'form': form})

def calc(request):
    if request.method == "POST":
        form = METForm(request.POST)
        age = request.POST.get("age")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        gender = request.POST.get("gender")
        mybmr  = bmrvalue(int(age),float(height),float(weight),gender)

        act_dict = {}

        for (key,value) in request.POST.lists():
            act_dict[key]=value
        if len(act_dict) > 1:
            count = len(act_dict['activity'])
            sumation = 0
            weeksum = 0
            cals = 0
            tothours = 0
            totmins = 0
            indiv = []
            total_cals = 0
            for value in range(count):
                print(act_dict['activity'][value], float(act_dict['level'][value]), int(act_dict['hours'][value]), int(act_dict['minutes'][value]))
                mymet = metvalue(float(act_dict['activity'][value].split('|')[1]), float(act_dict['level'][value]), int(act_dict['hours'][value]), int(act_dict['minutes'][value]))
                print(mymet)
                indiv_cals = float(mymet) * int(weight) * float(int(act_dict['hours'][value]) + (int(act_dict['minutes'][value])/60))
                total_cals += indiv_cals
                indivl= [act_dict['activity'][value].split('|')[0],int(act_dict['hours'][value]),int(act_dict['minutes'][value]),float(mymet),indiv_cals]
                indiv.append(indivl)
                sumation += mymet
                print(sumation)
                weeksum = sumation*7
                tothours += int(act_dict['hours'][value])
                totmins += int(act_dict['minutes'][value])
                if weeksum <= 2500:
                    remmet = 2500 - weeksum
                else:
                    remmet = 0
            return render (request , 'met_report.html', {'indiv':indiv, 'met':float(sumation), 'cals':float(total_cals), 'bmr':int(mybmr), 'weekmet':float(weeksum), 'remmet':float(remmet)})
        else:
            pdb.set_trace()
            return render (request , 'error_met.html')
    allact= mettable.objects.all()    
    context= {'allactivities': allact}
    return render (request , 'met_table.html' , context)
