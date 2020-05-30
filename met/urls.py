"""met URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]


from django.urls import path
from django.views.generic import RedirectView

from calculator import views

from simple import views as sv

urlpatterns = [
    path('bmr/', sv.BMR , name="bmr"),
    path('met/', sv.MET , name="met"),
    path('bmr_crispy/', views.METFormView.as_view(), name='bmr_crispy'),
    path('met_crispy/', views.METFormView.as_view(), name='met_crispy'),
    path('success/', views.SuccessView.as_view(), name='success'),
]

