from django.shortcuts import render
from . models import *
# Create your views here.

def Homepage(request):
    return render (request, "adminpages/home.html")

def AdminLogin(request):
    return render (request, "adminpages/admin_login.html")

def AdminHome(request):
    return render (request, "adminpages/admin_profile.html")

def Register(request):
    return render (request, "adminpages/Register.html")

def Login(request):
    return render (request, "adminpages/Login.html")

def Turfrequest(request):
    return render (request, "adminpages/turf_request.html")

def Adminaddmngr(request):
    return render (request, "adminpages/addmanager.html")

def Adminaddturf(request):
    return render (request, "adminpages/addturf.html")

def Adminfeedbacks(request):
    return render (request, "adminpages/admin_feed.html")

def Adminmanagers(request):
    return render (request, "adminpages/admin_manager.html")

def Adminusers(request):
    return render (request, "adminpages/admin_users.html")

def Adminturfs(request):
    return render (request, "adminpages/admin_turf.html")

def Adminrequests(request):
    return render (request, "adminpages/admin_requests.html")