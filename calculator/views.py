# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import BMRForm, METForm, CrispyAddressForm, CustomFieldForm
from django.shortcuts import render
# Create your views here.

'''
def bmrresult(age ,height ,weight , gender ):
    print("message2", file=sys.stderr)
    if gender == 'M':
        BMR = (10 * weight ) + (6.25 * height ) - (5 * age ) + 5
    else:
        BMR = (10 * weight ) + (6.25 * height ) - (5 * age ) - 161
    return BMR 


def MyBmr(request):
    if request.method == "POST":
        form = CrispyAddressForm(request.POST)
        if form.is_valid():
            age    = form.cleaned_data['age']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            gender = form.cleaned_data['gender']
            mybmr  = bmrvalue(age,height,weight,gender)
            form.save()
            return HttpResponse("BMR = "+ str(mybmr), content_type="text/plain")
            #return render (request , 'success.html', context={'bmr':mybmr })
        else:
            return HttpResponse("BMR = "+str(form.errors), content_type="text/plain")
    else:
        form = CrispyAddressForm()
        return render (request , 'bmr.html' , {'form': form})
'''
class BMRFormView(FormView):
    form_class = CrispyAddressForm
    success_url = reverse_lazy('success')
    template_name = 'bmr.html'

class METFormView(FormView):
    form_class = CustomFieldForm
    success_url = reverse_lazy('success')
    template_name = 'met.html'

class SuccessView(TemplateView):
    template_name = 'success.html'
