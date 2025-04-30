from .models import *
from django import forms



class PatientRegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
  
    class Meta:
        model = ParentReg
        fields = ('Childfirst_name','Childmiddle_name','Childlast_name','gender','DOB','POB','HOB','LOB','Motherfirst_name','Mothermiddle_name','Motherlast_name','Phone_number','username','password')
        widgets = {
            'DOB': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Select your birth date'
            }),
         
        }
        
        
    def save(self,commit=True):
         instance =super().save(commit=False)
         instance.password = make_password(self.cleaned_data['password'])  
        
         if commit:
            instance.save()
         return instance  
     
class PatientLoginForm(forms.Form): 

      username = forms.CharField(
          max_length=255,
          widget=forms.TextInput(attrs={
              'class':'form-control username-fields', 
              'placeholder':'Enter username'
              })
          )
      password = forms.CharField(max_length=255,widget=forms.PasswordInput(attrs={'class':'form-control password-fields', 'placeholder':'Enter username'}))
       
class AdminRegForm(forms.ModelForm):
      password= forms.CharField(widget=forms.PasswordInput)   
      
      class Meta:
          model = AdminPage
          fields = 'Firstname','Middlename','Lastname','Role','username','password'
          
      def save(self,commit=True):
          instance= super().save(commit=False) 
          instance.password = make_password(self.cleaned_data['password'])
         
          if commit:
               instance.save() 
          return instance    
      
class AdminLoginForm(forms.Form):
      username = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control username-fields','placeholder':'Enter Username'}))
      password = forms.CharField(max_length=255,widget=forms.PasswordInput(attrs={'class':'form-control password-fields','placholder':'Enter Password'}))

class DoctReportForm(forms.ModelForm):
    class Meta:
        model = DoctReport
        fields = ['date', 'wob', 'vaccination', 'new_date']     
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Select your birth date'
            }),
             'new_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Select your birth date'
            }),
         
        }
        
class DoctAttendanceForm(forms.ModelForm):
    class Meta:
        model = DoctAttendance
        fields = ['Attendance']     
     
class DoctNotificationForm(forms.ModelForm):
    class Meta:
        model = DoctNotification
        fields = ['Notification']     
     
        
