from django.shortcuts import render,redirect
from . models import *
from TMS_admin.models import Managerlist
from TMS_admin.views import *
# Create your views here.

def Managerhome(request):
    if 'managerlog_id' in request.session:
        id = request.session['managerlog_id']
        manager = Managerlist.objects.get(id = id)
        return render (request, "managerpages/Manager_profile.html", {'manager_data': manager})
    else:
        return render (request, "adminpages/LoginManager.html")
    
def Managerturf(request):
    if 'managerlog_id' in request.session:
        id = request.session['managerlog_id']
        manager = Managerlist.objects.get(id = id)
        return render (request, "managerpages/manager_turf.html", {'manager_data': manager})
    else:
        return render (request, "adminpages/LoginManager.html")

def Managerconfirm(request):
    if 'managerlog_id' in request.session:
        id = request.session['managerlog_id']
        manager = Managerlist.objects.get(id = id)
        return render (request, "managerpages/manag_confbook.html", {'manager_data': manager})
    else:
        return render (request, "adminpages/LoginManager.html")

def Managerbookings(request):
    if 'managerlog_id' in request.session:
        id = request.session['managerlog_id']
        manager = Managerlist.objects.get(id = id)
        return render (request, "managerpages/manag_bookhist.html", {'manager_data': manager})
    else:
        return render (request, "adminpages/LoginManager.html")

def Managerreviews(request):
    if 'managerlog_id' in request.session:
        id = request.session['managerlog_id']
        manager = Managerlist.objects.get(id = id)
        return render (request, "managerpages/manag_turfreview.html", {'manager_data': manager})
    else:
        return render (request, "adminpages/LoginManager.html")

def Managereditturf(request, turf_id):
    if 'managerlog_id' in request.session:
        if request.method == "POST":
            t_name = request.POST['turfname1']
            t_location = request.POST['turfloc1']
            t_desc = request.POST['turfdesc1']
            Managerlist.objects.filter(id = turf_id).update(man_turfname = t_name, man_turfloc = t_location, turf_desc = t_desc)
            return redirect('manager:mturf')
        else:
            manager = Managerlist.objects.get(id = turf_id)    
            return render (request, "managerpages/manag_editturf.html", {'manager_data': manager})
    else:
        return render (request, "adminpages/LoginManager.html")

def Managereditprofile(request,edit_id):
    if 'managerlog_id' in request.session:
        if request.method == "POST":
            m_name = request.POST['mngname']
            m_contact = request.POST['mngphone']
            m_email = request.POST['mngemail']
            m_username = request.POST['mngusername']
            m_password = request.POST['mngnewpass']
            Managerlist.objects.filter(id = edit_id).update(man_name=m_name, man_email=m_email, man_contact=m_contact, man_username=m_username, man_password=m_password)
            return redirect ('manager:mhomepage')
        else:    
            mng_data = Managerlist.objects.get(id = edit_id)
            return render (request, "managerpages/managerprofile2.html", {'mng': mng_data})
            
    else:
        return render (request, "adminpages/LoginManager.html")