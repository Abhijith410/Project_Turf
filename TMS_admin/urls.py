from django.urls import path
from . import views
app_name = 'appadmin'

urlpatterns = [
    path('Amalgamation/', views.Homepage, name = "homepage"),
    path('LoginUser/', views.Loginuser, name = "loginuser"),
    path('LoginManager/', views.Loginmanager, name = "loginmanager"),
    path('UserLogout/', views.Userlogout, name= "userlogout"),
    path('ManagerLogout/', views.Managerlogout, name= "managerlogout"),
    path('Contact/', views.Turfrequest, name = "turfrequest"),
    path('Register/', views.Register, name = "register"),
    path('Adminlogin/', views.AdminLogin, name = "admlogin"),
    path('Adminhome/', views.AdminHome, name = "admhome"),
    path('AdminLogout/', views.Adminlogout, name= "admlogout"),
    path('AdminAddmngr/<int:mn_id>', views.Adminaddmngr, name = "admaddmngr"),
    path('Adminrejectmngr/<int:mn_id>', views.Adminrejectmngr, name = "admreject"),
    path('AdminAddturf/', views.Adminaddturf, name = "admaddturf"),
    path('AdminFeedbacks/', views.Adminfeedbacks, name = "admfeedback"),
    path('AdminManagers/', views.Adminmanagers, name = "admmanagers"),
    path('AdminRejManagers/', views.Adminrejmanagers, name = "admrejmanagers"),
    path('AdminUsers/', views.Adminusers, name = "admusers"),
    path('AdminTurfs/', views.Adminturfs, name = "admturfs"),
    path('Adminimages/<int:turfid>', views.Adminviewimages, name = "admturfimages"),
    path('AdminRequests/', views.Adminrequests, name = "admrequests"),
]
