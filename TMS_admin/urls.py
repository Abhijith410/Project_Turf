from django.urls import path
from . import views
app_name = 'appadmin'

urlpatterns = [
    path('Amalgamation/', views.Homepage, name = "homepage"),
    path('Login/', views.Login, name = "login"),
    path('Contact/', views.Turfrequest, name = "turfrequest"),
    path('Register/', views.Register, name = "register"),
    path('Adminlogin/', views.AdminLogin, name = "admlogin"),
    path('Adminhome/', views.AdminHome, name = "admhome"),
    path('AdminAddmngr/', views.Adminaddmngr, name = "admaddmngr"),
    path('AdminAddturf/', views.Adminaddturf, name = "admaddturf"),
    path('AdminFeedbacks/', views.Adminfeedbacks, name = "admfeedback"),
    path('AdminManagers/', views.Adminmanagers, name = "admmanagers"),
    path('AdminUsers/', views.Adminusers, name = "admusers"),
    path('AdminTurfs/', views.Adminturfs, name = "admturfs"),
    path('AdminRequests/', views.Adminrequests, name = "admrequests"),
]