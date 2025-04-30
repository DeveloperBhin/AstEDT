from django.db import models
from django.contrib.auth.hashers import make_password,check_password





class AdminPage(models.Model):
      Firstname = models.CharField(max_length=255,default=None,blank=True,null=True)   
      Middlename = models.CharField(max_length=255,default=None,blank=True,null=True)
      Lastname = models.CharField(max_length=255,default=None,blank=True,null=True)
      username = models.CharField(max_length=255,default=None,blank=True,null=True)
      Role = models.CharField(max_length=20,choices=[("Admin", "Admin"), ("Doctor", "Doctor")],default="Doctor") 
      password = models.CharField(max_length=255,default=None,blank=True,null=True)
      
      def __str__(self):
          return self.Firstname()
      def set_password(self,raw_password):
          self.password = make_password(raw_password,self.password)
          
      def check_password(self,raw_password):
          
          return check_password(raw_password,self.password) 

class ParentReg(models.Model):
    admin = models.ForeignKey(AdminPage,on_delete=models.CASCADE, default=None)
    Childfirst_name = models.CharField(max_length=255,default=None,blank=True,null=True)
    Childmiddle_name = models.CharField(max_length=255,default=None,blank=True,null=True)
    Childlast_name = models.CharField(max_length=255,default=None,blank=True,null=True)
    gender = models.CharField(max_length=20,choices=[("Male","Male"),("Female","Female")],default=None)
    DOB = models.DateField(default=None) #DOB=Place of Birth
    POB = models.CharField(max_length=255,default=None,blank=True,null=True) #POB = Place Of Birth
    HOB = models.DecimalField(max_digits=3,decimal_places=2,default=None,blank=True,null=True) #HOB = Height Of Birth
    LOB = models.DecimalField(max_digits=3,decimal_places=2,default=None,blank=True,null=True) #LOB = Length of birth
    Motherfirst_name = models.CharField(max_length=255,default=None,blank=True,null=True)
    Mothermiddle_name = models.CharField(max_length=255,default=None,blank=True,null=True)
    Motherlast_name = models.CharField(max_length=255,default=None,blank=True,null=True)
    Phone_number = models.BigIntegerField()
    username = models.CharField(max_length=255,default=None,blank=True,null=True)
    password = models.CharField(max_length=255,default=None,null=True,blank=True)
    
    
    def __str__(self):
        return self.Childfirst_name
    def set_password(self, raw_password):
        """Sets the password after hashing it."""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Checks if the provided password matches the stored hashed password."""
        return check_password(raw_password, self.password)
   
      

class DoctAttendance(models.Model):
    parent = models.ForeignKey(ParentReg,on_delete=models.CASCADE, default=None)
    child_first_name = models.CharField(max_length=255, blank=True, null=True)
    child_middle_name = models.CharField(max_length=255, blank=True, null=True)
    child_last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=[("Male", "Male"), ("Female", "Female")])
    dob = models.DateField(default=None)
    pob = models.CharField(max_length=255, blank=True, null=True)
    hob = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    lob = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    mother_first_name = models.CharField(max_length=255, blank=True, null=True)
    mother_middle_name = models.CharField(max_length=255, blank=True, null=True)
    mother_last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.BigIntegerField(default=None)
    username = models.CharField(max_length=255, blank=True, null=True)
    Attendance = models.CharField(max_length=20, choices=[("Attend","Attend"),("Not Attend","Not Attend")],default=None)


  
class DoctReport(models.Model):
    parent = models.ForeignKey(ParentReg,on_delete=models.CASCADE, default=None)
    child_first_name = models.CharField(max_length=255, blank=True, null=True)
    child_middle_name = models.CharField(max_length=255, blank=True, null=True)
    child_last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=[("Male", "Male"), ("Female", "Female")])
    dob = models.DateField(default=None)
    pob = models.CharField(max_length=255, blank=True, null=True)
    hob = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    lob = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    mother_first_name = models.CharField(max_length=255, blank=True, null=True)
    mother_middle_name = models.CharField(max_length=255, blank=True, null=True)
    mother_last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.BigIntegerField(default=None)
    username = models.CharField(max_length=255, blank=True, null=True)

    date = models.DateField(default=None)
    wob = models.DecimalField("New Weight", max_digits=12, decimal_places=2, blank=True, null=True)
    vaccination = models.CharField(max_length=20, choices=[("Vaccinated", "Vaccinated"), ("Not Vaccinated", "Not Vaccinated")],default=None)
    new_date = models.DateField(default=None)


class DoctNotification(models.Model):
    parent = models.ForeignKey(ParentReg,on_delete=models.CASCADE, default=None)
    child_first_name = models.CharField(max_length=255, blank=True, null=True)
    child_middle_name = models.CharField(max_length=255, blank=True, null=True)
    child_last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=[("Male", "Male"), ("Female", "Female")])
    dob = models.DateField(default=None)
    pob = models.CharField(max_length=255, blank=True, null=True)
    hob = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    lob = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    mother_first_name = models.CharField(max_length=255, blank=True, null=True)
    mother_middle_name = models.CharField(max_length=255, blank=True, null=True)
    mother_last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.BigIntegerField(default=None)
    username = models.CharField(max_length=255, blank=True, null=True)
    Notification = models.CharField(max_length=100, choices=[("Unakumbushwa kufika clinic siku ya kesho","Unakumbushwa kufika clinic siku ya kesho")],default=None)
    

