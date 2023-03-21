from django.urls import path
from . import views
app_name = 'user'

urlpatterns = [
    path('UserHome/', views.Userhome, name = "uhomepage"),
    path('UserSearch/', views.Usersearch, name = "usearchturf"),
    path('UserConfirm/<int:turfid>', views.Userconfirm, name = "uconfirmturf"),
    path('UserBookings/', views.Userbookings, name = "ubookings"),
    path('UserPayment/', views.Userpayment, name = "upayment"),
    path('UserFeedback/', views.Userfeedback, name = "ufeedback"),
    path('UserEditprofile/<int:edit_id>', views.Usereditprofile, name = "ueditprofile"),
]