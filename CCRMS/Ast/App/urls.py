
from django.urls import path
from . import views


urlpatterns = [
   path('',views.index,name='index'),
   path('DocReport/',views.DocReport,name='DocReport'),
   path('Attendance/',views.Attendance,name='Attendance'),
   path('Update/',views.Update,name='Update'),
   path('register/',views.PatientRegView,name='register'),
   path('Notification/',views.Notification,name='Notification'),
   path('Login/',views.Login,name='Login'),
   path('Dashboard/<int:pk>/',views.Dashboard,name='Dashboard'),
  path('AdminDashboard/',views.AdminDashboard,name='AdminDashboard'),
  path('DoctorDashboard/',views.DoctorDashboard,name='DoctorDashboard'),
  path('statistic/',views.statisticView,name='statistic'),
  path('AdminLogin/',views.AdminLogin,name='AdminLogin'),
  path('Adminregister/',views.AdminRegView,name='Adminregister'),
  path('DoctReport/<int:id>/',views.DoctReportView,name='DoctReport'),
  path('SearchPatient/',views.SearchPatientView,name='SearchPatient'),
  path('DoctPatient/',views.DoctPatientView,name='DoctPatient'),
  path('Attendance/<int:id>/',views.DoctAttendanceView,name='Attendance'),
  path('DoctAttend/',views.DoctAttendView,name='DoctAttend'),
  path('SearchReport/',views.SearchReportView,name='SearchReport'),
  path('Notification/<int:id>/',views.DoctNotificationView,name='Notification'),
  path('DoctNotify/',views.DoctNotifyView,name='DoctNotify'),
  path('SearchNotification/',views.SearchNotificationView,name='SearchNotification'),
  path('PatientReg_update/<int:pk>/',views.PatientReg_update,name='PatientReg_update'),
  path('DoctUpdates/',views.DoctUpdateView,name='DoctUpdates'),
  path('SearchUpdates/',views.SearchUpdatesView,name='SearchUpdates'),
  path('ReportParent/int:pk/',views.Reportparent,name='ReportParent'),
  path('ViewReport/<int:pk>/',views.ViewReport,name='ViewReport'),
  path('ViewAttendance/<int:pk>/',views.ViewAttendance,name='ViewAttendance'),
  path('ViewNotification/<int:pk>/',views.ViewNotification,name='ViewNotification'),
 
 
  
 

  
  
  
   
]

