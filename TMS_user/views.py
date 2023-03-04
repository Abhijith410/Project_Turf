from django.shortcuts import render
from . models import *
# Create your views here.

def Userhome(request):
    return render (request, "userpages/user_profile.html")

def Usersearch(request):
    return render (request, "userpages/user_srchturf.html")

def Userconfirm(request):
    return render (request, "userpages/user_confbook.html")

def Userbookings(request):
    return render (request, "userpages/user_bookings.html")

def Userpayment(request):
    return render (request, "userpages/user_pymnt.html")

def Userfeedback(request):
    return render (request, "userpages/user_feedbck.html")

def Usereditprofile(request):
    return render (request, "userpages/userprofile2.html")
