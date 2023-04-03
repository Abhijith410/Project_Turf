from django.urls import path
from . import views
app_name = 'manager'

urlpatterns = [
    path('ManagerHome/', views.Managerhome, name = "mhomepage"),
    path('ManagerTurf/', views.Managerturf, name = "mturf"),
    path('ManagerConfirm/', views.Managerconfirm, name = "mbookconfirm"),
    path('ManagerCancel/', views.Managercancel, name = "mcancelbook"),
    path('ManagerAccept/', views.Manageraccept, name = "macceptbook"),
    path('ManagerBookings/', views.Managerbookings, name = "mbookhistory"),
    path('ManagerReviews/', views.Managerreviews, name = "mturfreview"),
    path('ManagerEditturf/<int:turf_id>', views.Managereditturf, name = "mturfedit"),
    path('ManagerAddimage/', views.Manageraddimage, name = "mturfimage"),
    path('ManagerEditprofile/<int:edit_id>', views.Managereditprofile, name = "meditprofile"),
]