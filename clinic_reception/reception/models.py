from unittest.mock import DEFAULT
from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class Patient (models.Model):
    first_name = models.CharField(verbose_name="first name", max_length=50)
    middle_name = models.CharField(verbose_name="middle name", max_length=50)
    last_name = models.CharField(verbose_name="last name", max_length=50)
    code = models.PositiveIntegerField(verbose_name="patient code",unique=True,editable=False)
    gender_choices = [('M',"Male"),("F","female")]
    gender = models.CharField('gender', max_length=50,choices=gender_choices)
    date_of_birth = models.DateField(verbose_name='date of birth', auto_now=False, auto_now_add=False)
    address = models.CharField(verbose_name="address", max_length=200,null=True)
    post_code = models.CharField("postal code", max_length=50,null=True)
    phone = models.CharField("phone number", max_length=50,null=True)

    def __str__(self) -> str:
        return self.first_name+' '+self.last_name+'-'+str(self.code)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = get_random_string(6,"1234567890")
        return super(Patient, self).save(*args, **kwargs)

class ReferralPhysician(models.Model):
    first_name = models.CharField(verbose_name="firstname", max_length=50)
    last_name = models.CharField(verbose_name="last name", max_length=50)
    field = models.CharField(verbose_name="field of specialization",max_length=80)
    fee = models.DecimalField(verbose_name="referral fee", max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return 'DR '+self.first_name+' '+self.last_name

class Physician(models.Model):
    first_name = models.CharField(verbose_name="firstname", max_length=50)
    last_name = models.CharField(verbose_name="last name", max_length=50)
    field = models.CharField(verbose_name="field of specialization",max_length=80)
    user = models.OneToOneField(User,on_delete=models.SET_NULL ,null=True)

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
    code = models.CharField(verbose_name='invoice code',max_length=7,editable=False, unique=True)
    date = models.DateTimeField(verbose_name="reception date", auto_now=False, auto_now_add=False)
    Patient = models.ForeignKey(Patient, verbose_name="patient", on_delete=models.CASCADE)
    RefferalPhysician = models.ForeignKey(ReferralPhysician, verbose_name='refferal physician', on_delete=models.CASCADE,null=True,blank=True)
    services_mri = models.ManyToManyField(ServiceMri,blank=True,related_name="mri_services")
    services_ctscan = models.ManyToManyField(ServiceCtscan,blank=True)
    services_xray = models.ManyToManyField(ServiceXray,blank=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = get_random_string(6,"1234567890")
        return super(Invoice, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.code)+" "+ str(self.date)+(self.Patient.first_name)


class Expenses (models.Model):
    name = models.CharField(verbose_name="expense name",max_length=150)
    cost = models.DecimalField(verbose_name="cost", max_digits=8, decimal_places=2)
    quantity = models.IntegerField(verbose_name="quantity")
    date = models.DateField(verbose_name="date",auto_now=False, auto_now_add=False)