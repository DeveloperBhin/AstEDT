from django.shortcuts import render,redirect
from .models import *
from .forms import * 
from django.contrib.auth import logout,login,authenticate
from django.shortcuts import get_object_or_404
from django.contrib import messages



def index(request):
    return render(request, 'index.html')

def PatientRegView(request):
    if request.method == 'POST':
        username = request.POST['username']
        pateintreg = PatientRegForm(request.POST)

        
        if ParentReg.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        if pateintreg .is_valid():
            pateintreg.save()
            
            return redirect('Login')
        else:
         print(pateintreg .errors)
     
      
    else: 
     pateintreg  = PatientRegForm()
    
        
    
    context={
        'pateintreg':pateintreg 
       
    }
    
    return render(request, 'register.html',context)


def Login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = ParentReg.objects.get(username=username)
                if user.check_password(password):
                   request.session['patient_id'] = user.id
                   return redirect('Dashboard',pk=user.pk)
                else:
                   messages.error(request, "Invalid password.") 
                   
            except ParentReg.DoesNotExist:
                form.add_error(None, 'Invalid username or password')
    else:
        form = PatientLoginForm()

    return render(request, 'Login.html', {'form': form})

def AdminRegView(request):
    if request.method == 'POST':
        username = request.POST['username']
       
        Adminpg = AdminRegForm(request.POST)
        if AdminPage.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
       
        if Adminpg.is_valid():
            Adminpg.save()
            return redirect('AdminLogin')
        
    else:
        Adminpg = AdminRegForm()    
        
        
     
    
    return render(request,'AdminReg.html',{'Adminpg':Adminpg})

def AdminLogin(request):
    if request.method == 'POST':
       Loginform = AdminLoginForm(request.POST)
       if Loginform.is_valid():
        
        username = Loginform.cleaned_data['username']
        password = Loginform.cleaned_data['password']
       
       try:
           user = AdminPage.objects.get(username=username)
           
           if user.check_password(password):
              request.session['Admin_id'] = user.id
              if user.Role=='Admin':
               
              
               return redirect('AdminDashboard') 
              else:
               return redirect('DoctorDashboard')
           else:
               Loginform.add_error(None,'Invalid Username or Password')
               
       except AdminPage.DoesNotExist:
             Loginform.add_error(None,'Invalid Username or Password')
             
            
    else:
        Loginform = AdminLoginForm()
        
    context = {
        'Loginform':Loginform
    }             
        
    return render(request,'AdminLogin.html',context)


def DocReport(request):
    
    return render(request, 'DocReport.html')
def Attendance(request):
    return render(request, 'Attendance.html')
def Notification(request):
    return render(request,'Notification.html')
def Update(request):
    return render(request,'Update.html')
def Dashboard(request,pk):
    patient = get_object_or_404(ParentReg, pk=pk)
    
    return render(request, 'ChildrenDashboard.html', {'patient': patient})
def AdminDashboard(request):
    return render(request,'AdminDashboard.html')

def DoctorDashboard(request):
  return render(request,'DoctorDashboard.html')

def statisticView(request):
    return render(request, 'statistics.html')

def SearchPatientView(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        child = ParentReg.objects.filter(username__icontains=searched)
        return render(request, 'SearchPatient.html', {'searched': searched, 'child': child})
    else:
        return render(request, 'SearchPatient.html')



def DoctReportView(request, id):
    item = get_object_or_404(ParentReg, id=id)

    

    if request.method == 'POST':
        form = DoctReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)

            
            report.child_first_name = item.Childfirst_name
            report.child_middle_name = item.Childmiddle_name
            report.child_last_name = item.Childlast_name
            report.gender = item.gender
            report.dob = item.DOB
            report.pob = item.POB
            report.hob = item.HOB
            report.lob = item.LOB

            report.mother_first_name = item.Motherfirst_name
            report.mother_middle_name = item.Mothermiddle_name
            report.mother_last_name = item.Motherlast_name
            report.phone_number = item.Phone_number
            report.username = item.username
            report.parent = item

            report.save()
            return redirect('DoctPatient')
        else:
            print("Form Errors:", form.errors)
    else:
        form = DoctReportForm()

    return render(request, 'DoctReport.html', {
        'form': form,
        'item': item
    })

def DoctPatientView(request):
     child =ParentReg.objects.all()

     return render(request, 'DoctPatientView.html',{'child': child})


def DoctAttendanceView(request, id):
    item = get_object_or_404(ParentReg, id=id)
    
    
    if request.method == 'POST':
        form = DoctAttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)

  
            attendance.child_first_name = item.Childfirst_name
            attendance.child_middle_name = item.Childmiddle_name
            attendance.child_last_name = item.Childlast_name
            attendance.gender = item.gender
            attendance.dob = item.DOB
            attendance.pob = item.POB
            attendance.hob = item.HOB
            attendance.lob = item.LOB

            attendance.mother_first_name = item.Motherfirst_name
            attendance.mother_middle_name = item.Mothermiddle_name
            attendance.mother_last_name = item.Motherlast_name
            attendance.phone_number = item.Phone_number
            attendance.username = item.username
            attendance.patient = item  
          
            attendance.save()
            return redirect('DoctAttend')
        else:
            print("Form Errors:", form.errors)
    else:
        form = DoctAttendanceForm()

    return render(request, 'Attendance.html', {
        'form': form,
        'item': item
    })
def DoctAttendView(request):
     child =ParentReg.objects.all()

     return render(request, 'DoctAttendanceView.html',{'child': child})

def SearchReportView(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        child = ParentReg.objects.filter(username__icontains=searched)
        return render(request, 'SearchReport.html', {'searched': searched, 'child': child})
    else:
        return render(request, 'SearchReport.html')


def DoctNotificationView(request, id):
    item = get_object_or_404(ParentReg, id=id)
    
    
    if request.method == 'POST':
        form = DoctNotificationForm(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)

            
            notification.child_first_name = item.Childfirst_name
            notification.child_middle_name = item.Childmiddle_name
            notification.child_last_name = item.Childlast_name
            notification.gender = item.gender
            notification.dob = item.DOB
            notification.pob = item.POB
            notification.hob = item.HOB
            notification.lob = item.LOB

            notification.mother_first_name = item.Motherfirst_name
            notification.mother_middle_name = item.Mothermiddle_name
            notification.mother_last_name = item.Motherlast_name
            notification.phone_number = item.Phone_number
            notification.username = item.username
            notification.patient = item  
          
            notification.save()
            return redirect('DoctNotify')
        else:
            print("Form Errors:", form.errors)
    else:
        form = DoctNotificationForm()

    return render(request, 'Notification.html', {
        'form': form,
        'item': item
    })
def DoctNotifyView(request):
     child =ParentReg.objects.all()

     return render(request, 'DoctNotification.html',{'child': child})

def SearchNotificationView(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        child = ParentReg.objects.filter(username__icontains=searched)
        return render(request, 'SearchNotification.html', {'searched': searched, 'child': child})
    else:
        return render(request, 'SearchNotification.html')


def PatientReg_update(request, pk):
    patient = get_object_or_404(ParentReg, pk=pk)
    form = PatientRegForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        return redirect('DoctorDashboard')
    return render(request, 'Update.html', {'form': form})

def DoctUpdateView(request):
     form =ParentReg.objects.all()

     return render(request, 'DoctUpdate.html',{'form': form})


def SearchUpdatesView(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        child = ParentReg.objects.filter(username__icontains=searched)
        return render(request, 'SearchUpdates.html', {'searched': searched, 'child': child})
    else:
        return render(request, 'SearchUpdates.html')
    
def Reportparent(request, pk):
    patient = get_object_or_404(ParentReg, pk=pk)
    form = DoctReportForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        return redirect('ChildrenDashboard')
    return render(request, 'ChildrenDashboard.html', {'form': form})

def DoctUpdateView(request):
     form =ParentReg.objects.all()

     return render(request, 'DoctUpdate.html',{'form': form})

def ViewReport(request,pk):
    parent = DoctReport.objects.filter(parent=pk)
    
    return render(request, 'Viewreport.html', {'parent': parent})


def ViewAttendance(request,pk):
    patient = get_object_or_404(DoctAttendance, pk=pk)
    
    return render(request, 'Viewattendance.html', {'patient': patient})



def ViewNotification(request,pk):
    patient = get_object_or_404(DoctNotification, pk=pk)
    
    return render(request, 'Viewnotification.html', {'patient': patient})
