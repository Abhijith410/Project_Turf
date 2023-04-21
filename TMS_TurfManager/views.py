from django.shortcuts import render,redirect
from . models import *
from TMS_admin.models import Managerlist
from TMS_admin.models import Turfimages
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
        image = Turfimages.objects.filter(manager_id = id)
        return render (request, "managerpages/manager_turf.html", {'manager_data': manager, 't_image': image})
    else:
        return render (request, "adminpages/LoginManager.html")

def Managerconfirm(request):
    if 'managerlog_id' in request.session:
        id = request.session['managerlog_id']
        manager = Managerlist.objects.get(id = id)
        booking = Bookings.objects.filter(mn_id_id = id, b_status = 'Pending')
        return render (request, "managerpages/manag_confbook.html", {'manager_data': manager, 'bookings': booking})
    else:
        return render (request, "adminpages/LoginManager.html")

def Managerbookings(request):
    if 'managerlog_id' in request.session:
        id = request.session['managerlog_id']
        manager = Managerlist.objects.get(id = id)
        booking = Bookings.objects.filter(mn_id_id = id)
        return render (request, "managerpages/manag_bookhist.html", {'manager_data': manager, 'bookings': booking})
    else:
        return render (request, "adminpages/LoginManager.html")

def Managercancel(request):
    if 'managerlog_id' in request.session:
        id = request.session['managerlog_id']
        status = 'Cancelled'
        payment = 'NA'
        Bookings.objects.filter(mn_id_id = id).update(b_status = status, b_pstatus = payment)
        return redirect ('manager:mbookhistory')
    else:
        return render (request, "adminpages/LoginManager.html")
    
def Manageraccept(request):
    if 'managerlog_id' in request.session:
        id = request.session['managerlog_id']
        status = 'Confirmed'
        payment = 'Pending'
        Bookings.objects.filter(mn_id_id = id).update(b_status = status, b_pstatus = payment)
        return redirect ('manager:mbookhistory')
    else:
        return render (request, "adminpages/LoginManager.html")    

def Managerreviews(request):
    if 'managerlog_id' in request.session:
        id = request.session['managerlog_id']
        manager = Managerlist.objects.get(id = id)
        review = Turfreview.objects.filter(m_id_id = id)
        return render (request, "managerpages/manag_turfreview.html", {'manager_data': manager, 'reviews': review})
    else:
        return render (request, "adminpages/LoginManager.html")

def Managereditturf(request, turf_id):
    if 'managerlog_id' in request.session:
        if request.method == "POST":
            t_name = request.POST['turfname1']
            t_location = request.POST['turfloc1']
            t_cost = request.POST['turfcost1']
            t_desc = request.POST['turfdesc1']
            Managerlist.objects.filter(id = turf_id).update(man_turfname = t_name, man_turfloc = t_location, turf_cost = t_cost, turf_desc = t_desc)
            return redirect('manager:mturf')
        else:
            manager = Managerlist.objects.get(id = turf_id)    
            return render (request, "managerpages/manag_editturf.html", {'manager_data': manager})
    else:
        return render (request, "adminpages/LoginManager.html")
    
def Manageraddimage(request):
    if 'managerlog_id' in request.session:
        m_id = request.session['managerlog_id']
        if request.method == "POST":
            t_image = request.FILES['image']
            Turf = Turfimages(images = t_image, manager_id_id = m_id)
            Turf.save()
            return redirect('manager:mturf')
        else:
            manager = Managerlist.objects.get(id = m_id)
            return render (request, "managerpages/manag_turfimage.html", {'manager_data': manager})
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