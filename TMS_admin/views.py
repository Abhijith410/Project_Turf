from django.shortcuts import render, redirect
from . models import *
from TMS_user.views import *
from TMS_TurfManager.views import *

# Create your views here.

def Homepage(request):
    return render (request, "adminpages/home.html")

def Homepage2(request):
    return render (request, "adminpages/home2.html")

def AdminLogin(request):
    if request.method == "POST":
        adminname = request.POST['adname']
        adminpass = request.POST['adpass']
        try:
            admin_log = Adminlog.objects.get(admin_name = adminname, admin_pass = adminpass)
            request.session['adlog_id'] = admin_log.id
            return redirect ('appadmin:admhome')
        except Adminlog.DoesNotExist:
            return render (request, "adminpages/admin_login.html", {'failed':'Login credentials incorrect'}) 
    return render (request, "adminpages/admin_login.html")

def AdminHome(request):
    if 'adlog_id' in request.session:
        return render (request, "adminpages/admin_profile.html")
    else:
        return render (request, "adminpages/admin_login.html")
    
def Adminlogout(request):
    del request.session['adlog_id']
    return redirect ('appadmin:admlogin')

def Adminaddmngr(request,mn_id):
    if 'adlog_id' in request.session:
        if request.method == "POST":
            m_name = request.POST['mngrname']
            m_contact = request.POST['mngrcontact']
            m_email = request.POST['mngrmail']
            m_turfname = request.POST['mngrturf']
            m_turfloc = request.POST['mngrturfloc']
            m_username = request.POST['mngrid']
            m_password = request.POST['mngrpass']
            m_status = 'accepted'
            Managerlist.objects.filter(id=mn_id).update(man_name=m_name, man_email=m_email, man_contact=m_contact, man_turfname = m_turfname, man_turfloc=m_turfloc, man_username=m_username, man_password=m_password, man_status = m_status)
            return redirect ('appadmin:admrequests')
        else:    
            mng_data = Managerlist.objects.get(id=mn_id)
            return render (request, "adminpages/addmanager.html", {'mng': mng_data})
            
    else:
        return render (request, "adminpages/admin_login.html")

def Adminrejectmngr(request,mn_id):
    if 'adlog_id' in request.session:
        man_status = 'rejected'
        Managerlist.objects.filter(id=mn_id).update(man_status = man_status)
        return redirect ('appadmin:admrequests')
    else:
        return render (request, "adminpages/admin_login.html")

def Adminaddturf(request):
    if 'adlog_id' in request.session:
        return render (request, "adminpages/addturf.html")
    else:
        return render (request, "adminpages/admin_login.html")
    
def Adminfeedbacks(request):
    if 'adlog_id' in request.session:
        us_feed = Feedbacks.objects.all().order_by('id')
        return render (request, "adminpages/admin_feed.html", {'feed':us_feed})
    else:
        return render (request, "adminpages/admin_login.html")
    
def Adminmanagers(request):
    if 'adlog_id' in request.session:
        mr_data = Managerlist.objects.filter(man_status = 'accepted').order_by('id')
        return render (request, "adminpages/admin_manager.html", {'m_data':mr_data})
    else:
        return render (request, "adminpages/admin_login.html")
    
def Adminrejmanagers(request):
    if 'adlog_id' in request.session:
        rmr_data = Managerlist.objects.filter(man_status = 'rejected').order_by('id')
        return render (request, "adminpages/admin_manager_reject.html", {'rm_data':rmr_data})
    else:
        return render (request, "adminpages/admin_login.html")    

def Adminusers(request):
    if 'adlog_id' in request.session:
        user_data = Userlist.objects.all().order_by('id')
        return render (request, "adminpages/admin_users.html", {'u_data':user_data})
    else:
        return render (request, "adminpages/admin_login.html")  

def Adminturfs(request):
    if 'adlog_id' in request.session:
        turf_data = Managerlist.objects.filter(man_status = 'accepted').order_by('id')
        return render (request, "adminpages/admin_turf.html", {'t_data':turf_data})
    else:
        return render (request, "adminpages/admin_login.html")
    
def Adminviewimages(request,turfid):
    if 'adlog_id' in request.session:
        turf_data = Managerlist.objects.get(id = turfid)
        turfimages = Turfimages.objects.filter(manager_id = turfid)
        return render (request, "adminpages/admin_turfdetails.html", {'t_data':turf_data, 'image': turfimages})
    else:
        return render (request, "adminpages/admin_login.html")   

def Adminrequests(request):
    if 'adlog_id' in request.session:
        request_data = Managerlist.objects.filter(man_status = 'Pending')
        return render (request, "adminpages/admin_requests.html", {'req_data':request_data})
    else:
        return render (request, "adminpages/admin_login.html")
    
def Register(request):
    regmessage = ""
    if request.method == "POST":
        u_name = request.POST['regname']
        u_email = request.POST['regmail']
        u_number = request.POST['regnumber']
        u_username = request.POST['regusername']
        u_password = request.POST['regpass']
        u_confpassword = request.POST['regconfpass']
        reg_data = Userlist(user_name = u_name, user_email = u_email, user_mobile = u_number, user_username = u_username, user_password = u_password, user_confpassword = u_confpassword)
        reg_data.save()
        if reg_data:
            regmessage = "Registered successfully. Now you can login to your account."
        else:
            regmessage = "error"
    return render (request, "adminpages/Register.html", {'reg': regmessage})

def Loginuser(request):
    if request.method == 'POST':
        username = request.POST['logusername']
        password = request.POST['loguserpass']
        try:
            user = Userlist.objects.get(user_username = username, user_password = password)
            request.session['userlog_id'] = user.id
            return redirect('user:uhomepage')
        except Userlist.DoesNotExist:
            return render (request, "adminpages/LoginUser.html", {'fail':'No user found.'})
    return render (request, "adminpages/LoginUser.html")     

def Userlogout(request):
    del request.session['userlog_id']
    # return render (request, "adminpages/LoginUser.html", {'logout':'You have successfully logged out.'})
    return redirect ('appadmin:loginuser')

def Loginmanager(request):
    if request.method == 'POST':
        username = request.POST['logmngrusername']
        password = request.POST['logmngrpass']
        try:
            manager = Managerlist.objects.get(man_username = username, man_password = password)
            request.session['managerlog_id'] = manager.id
            if manager.man_status == 'accepted':
                return redirect('manager:mhomepage')
            else:
                return render (request, "adminpages/LoginManager.html", {'fail':'Invalid Login credentials!!!'})
        except Managerlist.DoesNotExist:
            return render (request, "adminpages/LoginManager.html", {'fail':'No Manager found.'})
    return render (request, "adminpages/LoginManager.html")  

def Managerlogout(request):
    del request.session['managerlog_id']
    # return render (request, "adminpages/LoginManager.html", {'logout':'You have successfully logged out.'})
    return redirect ('appadmin:loginmanager')

def Turfrequest(request):
    rmessage = ""
    if request.method == "POST":
        mng_name = request.POST['treqname']
        mng_email = request.POST['treqmail']
        mng_contact = request.POST['treqnumber']
        mng_turfname = request.POST['treqturfname']
        mng_turfloc = request.POST['treqturfloc']
        mng_username = request.POST['treqmngrusname']
        mng_pass = request.POST['treqmngrpass']
        mng_status = "Pending"
        mng_data = Managerlist(man_name=mng_name, man_email=mng_email, man_contact=mng_contact, man_turfname=mng_turfname, man_turfloc=mng_turfloc, man_username=mng_username, man_password=mng_pass, man_status=mng_status)
        mng_data.save()
        if mng_data:
            rmessage = "Thank you for entering the details. Please wait for the confirmation."
        else:
            rmessage = "error"    
    return render (request, "adminpages/turf_request.html", {'req': rmessage})  