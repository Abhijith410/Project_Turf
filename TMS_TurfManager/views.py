from django.shortcuts import render
from . models import *
# Create your views here.

def Managerhome(request):
    return render (request, "managerpages/Manager_profile.html")

def Managerturf(request):
    return render (request, "managerpages/manager_turf.html")

def Managerconfirm(request):
    return render (request, "managerpages/manag_confbook.html")

def Managerbookings(request):
    return render (request, "managerpages/manag_bookhist.html")

def Managerreviews(request):
    return render (request, "managerpages/manag_turfreview.html")

def Managereditturf(request):
    return render (request, "managerpages/manag_editturf.html")

def Managereditprofile(request):
    return render (request, "managerpages/managerprofile2.html")