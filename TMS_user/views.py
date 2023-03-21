from django.shortcuts import render, redirect
from . models import *
from TMS_admin.models import Userlist
from TMS_admin.models import Managerlist
from TMS_admin.models import Turfimages

# Create your views here.

def Userhome(request):
    if 'userlog_id' in request.session:
        userid = request.session['userlog_id']
        userlog = Userlist.objects.get(id = userid)
        return render (request, "userpages/user_profile.html", {'user': userlog})
    else:
        return render (request, "adminpages/LoginUser.html")

def Usersearch(request):
    if 'userlog_id' in request.session:
        userid = request.session['userlog_id']
        userlog = Userlist.objects.get(id = userid)
        turflist = Managerlist.objects.filter(man_status = 'accepted').all().order_by('id')
        turfimages = Turfimages.objects.all()
        return render (request, "userpages/user_srchturf.html", {'user': userlog, 'turf': turflist, 'imageturf': turfimages})
    else:
        return render (request, "adminpages/LoginUser.html")

def Userconfirm(request,turfid):
    if 'userlog_id' in request.session:
        userid = request.session['userlog_id']
        userlog = Userlist.objects.get(id = userid)
        turf_details = Managerlist.objects.get(id = turfid)
        return render (request, "userpages/user_confbook.html", {'user': userlog, 'turfdetails': turf_details})
    else:
        return render (request, "adminpages/LoginUser.html")

def Userbookings(request):
    if 'userlog_id' in request.session:
        userid = request.session['userlog_id']
        userlog = Userlist.objects.get(id = userid)
        return render (request, "userpages/user_bookings.html", {'user': userlog})
    else:
        return render (request, "adminpages/LoginUser.html")

def Userpayment(request):
    if 'userlog_id' in request.session:
        return render (request, "userpages/user_pymnt.html")
    else:
        return render (request, "adminpages/LoginUser.html")

def Userfeedback(request):
    if 'userlog_id' in request.session:
        userid = request.session['userlog_id']
        userlog = Userlist.objects.get(id = userid)
        fmessage = ""
        if request.method == "POST":
            name = request.POST['fname']
            email = request.POST['fmail']
            contact = request.POST['fcontact']
            desc = request.POST['fdesc']
            feedback = Feedbacks(f_name = name, f_email = email, f_contact = contact, f_message = desc)
            feedback.save()
            if feedback:
                fmessage = "Message recorded successfully"
            else:
                fmessage = "error"    
        return render (request, "userpages/user_feedbck.html", {'user': userlog, 'msg': fmessage})
    else:
        return render (request, "adminpages/LoginUser.html")

def Usereditprofile(request,edit_id):
    if 'userlog_id' in request.session:
        if request.method == "POST":
            name = request.POST['name1']
            email = request.POST['email1']
            phone = request.POST['phone1']
            username = request.POST['username1']
            password = request.POST['password1']
            Userlist.objects.filter(id = edit_id).update(user_name = name, user_email = email, user_mobile = phone, user_username = username, user_password = password)
            return redirect ('user:uhomepage')
        else:
            user_data = Userlist.objects.get(id = edit_id)
            return render (request, "userpages/userprofile2.html", {'usdata': user_data})
    else:
        return render (request, "adminpages/LoginUser.html")
