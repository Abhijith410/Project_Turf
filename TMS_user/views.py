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
        # turfimages = Turfimages.objects.filter(manager_id_id = userid)    
        review = Turfreview.objects.filter(m_id_id = userid)
        return render (request, "userpages/user_srchturf.html", {'user': userlog, 'turf': turflist,  'reviews': review})
    else:
        return render (request, "adminpages/LoginUser.html")
    
def Searchlist(request):
    if 'userlog_id' in request.session:
        userid = request.session['userlog_id']
        userlog = Userlist.objects.get(id = userid)
        searchname = request.POST['search']
        turflist = Managerlist.objects.filter(man_turfname__icontains=searchname, man_status = 'accepted').all().order_by('id')
        if searchname == "":
            return redirect('user:usearchturf')
        else:
            return render (request, "userpages/user_searchlist.html", {'user': userlog, 'turf1': turflist})
    else:
        return render (request, "adminpages/LoginUser.html")    
    
def Userreview(request,turfid):
    if 'userlog_id' in request.session:
        userid = request.session['userlog_id']
        userlog = Userlist.objects.get(id = userid)
        turf = Managerlist.objects.get(id = turfid)
        rmessage = ""
        if request.method == "POST":
            name = request.POST['revname']
            contact = request.POST['revcontact']
            message = request.POST['revmessage']
            us_review = Turfreview(u_id = userid, m_id = turf.id, r_name = name, r_contact = contact, r_message = message)
            us_review.save()
            if us_review:
                rmessage = "Thanks for your valuable feedback"
            else:
                rmessage = "error"
        return render (request, "userpages/user_review.html", {'user': userlog, 'turf': turf, 'msg': rmessage})
    else:
        return render (request, "adminpages/LoginUser.html")

def Userconfirm(request,turfid):
    if 'userlog_id' in request.session:
        userid = request.session['userlog_id']
        userlog = Userlist.objects.get(id = userid)
        turf_details = Managerlist.objects.get(id = turfid)
        bmessage = ""
        if request.method == "POST":
            name = request.POST['us_name']
            contact = request.POST['us_contact']
            turf = request.POST['us_turf']
            cost = request.POST['us_cost']
            date = request.POST['us_date']
            start = request.POST['us_start']
            end = request.POST['us_end']
            tcost = request.POST['us_totalcost']
            bstatus = "Pending"
            pstatus = "Pending"
            booking = Bookings(b_name=name, b_contact=contact, b_turf=turf, b_cost=cost, b_date=date, b_tst=start, b_tend=end, b_tcost=tcost, b_status=bstatus, b_pstatus=pstatus,mn_id_id=turf_details.id, us_id_id=userid)
            booking.save()
            if booking:
                bmessage = "Booking Details Submitted."
            else:
                bmessage = "error"
        return render (request, "userpages/user_confbook.html", {'user': userlog, 'turfdetails': turf_details, 'msg': bmessage})
    else:
        return render (request, "adminpages/LoginUser.html")

def Userbookings(request):
    if 'userlog_id' in request.session:
        userid = request.session['userlog_id']
        userlog = Userlist.objects.get(id = userid)
        booking = Bookings.objects.filter(us_id_id = userid)
        return render (request, "userpages/user_bookings.html", {'user': userlog, 'bookings': booking})
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