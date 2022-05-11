from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.forms import modelformset_factory


class Patient (models.Model):
    first_name = models.CharField(verbose_name="first name", max_length=50)
    middle_name = models.CharField(verbose_name="middle name", max_length=50)
    last_name = models.CharField(verbose_name="last name", max_length=50)
    code = models.PositiveIntegerField(verbose_name="patient code",unique=True)
    gender_choices = [('M',"Male"),("F","female")]
    gender = models.CharField('gender', max_length=50,choices=gender_choices)
    date_of_birth = models.DateField(verbose_name='date of birth', auto_now=False, auto_now_add=False)
    address = models.CharField(verbose_name="address", max_length=200,null=True)
    post_code = models.CharField("postal code", max_length=50,null=True)
    phone = models.CharField("phone number", max_length=50,null=True)

    def __str__(self) -> str:
        return self.first_name+' '+self.last_name+'-'+str(self.code)

class RefferalPhysician(models.Model):
    first_name = models.CharField(verbose_name="firstname", max_length=50)
    last_name = models.CharField(verbose_name="last name", max_length=50)
    field = models.CharField(verbose_name="field of specialization",max_length=80)
    fee = models.DecimalField(verbose_name="refferal fee", max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return 'DR '+self.first_name+' '+self.last_name

class Physician(models.Model):
    first_name = models.CharField(verbose_name="firstname", max_length=50)
    last_name = models.CharField(verbose_name="last name", max_length=50)
    field = models.CharField(verbose_name="field of specialization",max_length=80)

    def __str__(self) -> str:
        return 'DR '+self.first_name+' '+self.last_name

class ServiceMri (models.Model):
    name = models.CharField(verbose_name="service name",max_length=50)
    physician = models.ForeignKey(Physician,on_delete=models.CASCADE)
    fee = models.DecimalField(verbose_name="service fee",max_digits=6,decimal_places=2)
    
    def __str__(self) -> str:
        return self.name+'-'+str(self.physician)

class ServiceCtscan (models.Model):
    name = models.CharField(verbose_name="service name",max_length=50)
    physician = models.ForeignKey(Physician,on_delete=models.CASCADE)
    fee = models.DecimalField(verbose_name="service fee",max_digits=6,decimal_places=2)
    
    def __str__(self) -> str:
        return self.name+'-'+str(self.physician)

class ServiceXray (models.Model):
    name = models.CharField(verbose_name="service name",max_length=50)
    physician = models.ForeignKey(Physician,on_delete=models.CASCADE)
    fee = models.DecimalField(verbose_name="service fee",max_digits=6,decimal_places=2)
    
    def __str__(self) -> str:
        return self.name+'-'+str(self.physician)


class Invoice (models.Model):
    code = models.PositiveIntegerField(verbose_name='invoice code')
    date = models.DateTimeField(verbose_name="reception date", auto_now=False, auto_now_add=False)
    Patient = models.ForeignKey(Patient, verbose_name="patient", on_delete=models.CASCADE)
    RefferalPhysician = models.ForeignKey(RefferalPhysician, verbose_name='refferal physician', on_delete=models.CASCADE)
    services_mri = models.ManyToManyField(ServiceMri)
    services_ctscan = models.ManyToManyField(ServiceCtscan)
    services_xray = models.ManyToManyField(ServiceXray)

    def __str__(self) -> str:
        return str(self.code)+ str(self.date)


class Expenses (models.Model):
    name = models.CharField(verbose_name="expense name",max_length=150)
    cost = models.DecimalField(verbose_name="cost", max_digits=8, decimal_places=2)
    quantity = models.IntegerField(verbose_name="quantity")
    date = models.DateField(verbose_name="date",auto_now=False, auto_now_add=False)