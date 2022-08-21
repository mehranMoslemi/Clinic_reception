
from django.db import models
from django.contrib.auth.models import User



class Patient (models.Model):
    first_name = models.CharField(verbose_name="first name", max_length=50)
    middle_name = models.CharField(verbose_name="middle name", max_length=50)
    last_name = models.CharField(verbose_name="last name", max_length=50)
    gender_choices = [('M',"Male"),("F","female")]
    gender = models.CharField('gender', max_length=50,choices=gender_choices)
    date_of_birth = models.DateField(verbose_name='date of birth', auto_now=False, auto_now_add=False)
    address = models.CharField(verbose_name="address", max_length=200,null=True)
    post_code = models.CharField("postal code", max_length=50,null=True)
    phone = models.CharField("phone number", max_length=50,null=True)

    def __str__(self) -> str:
        return self.first_name+' '+self.middle_name+' '+self.last_name

    def name(self):
        return self.first_name+' '+self.middle_name+' '+self.last_name


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
    class Meta:
        verbose_name = "Examination (MRI)"
        verbose_name_plural = 'Examinations (MRI)'
        
    name = models.CharField(verbose_name="examination name",max_length=50)
    physician = models.ForeignKey(Physician,on_delete=models.CASCADE)
    fee = models.DecimalField(verbose_name="examination fee",max_digits=6,decimal_places=2)
    
    def __str__(self) -> str:
        return self.name+'-'+str(self.physician)

class ServiceCtscan (models.Model):
    class Meta:
        verbose_name = "Examination (CT-Scan)"
        verbose_name_plural = 'Examinations (CT-Scan)'
    name = models.CharField(verbose_name="examination name",max_length=50)
    physician = models.ForeignKey(Physician,on_delete=models.CASCADE)
    fee = models.DecimalField(verbose_name="examination fee",max_digits=6,decimal_places=2)
    
    def __str__(self) -> str:
        return self.name+'-'+str(self.physician)

class ServiceXray (models.Model):
    class Meta:
        verbose_name = "Examination (X-Ray)"
        verbose_name_plural = 'Examinations (X-Ray)'
    name = models.CharField(verbose_name="examination name",max_length=50)
    physician = models.ForeignKey(Physician,on_delete=models.CASCADE)
    fee = models.DecimalField(verbose_name="examination fee",max_digits=6,decimal_places=2)
    
    def __str__(self) -> str:
        return self.name+'-'+str(self.physician)


class Mri_Invoice (models.Model):
    class Meta:
        verbose_name = "Invoice (MRI)"
        verbose_name_plural = 'Invoices (MRI)'

    date = models.DateField(verbose_name="reception date", auto_now=False, auto_now_add=False)
    time = models.TimeField(verbose_name="reception time", auto_now=False, auto_now_add=False)
    Patient = models.ForeignKey(Patient, verbose_name="patient", on_delete=models.CASCADE)
    RefferalPhysician = models.ForeignKey(ReferralPhysician, verbose_name='refferal physician', on_delete=models.CASCADE,null=True,blank=True)
    services_mri = models.ManyToManyField(ServiceMri,blank=True,related_name="mri_services")
    discount = models.DecimalField(verbose_name='discount', max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return str(self.id)+" "+ str(self.date)+(self.Patient.first_name)

    def patient_name(self):
        return str(self.Patient)
    
    def total_fee(self):
        total = 0
        for service in self.services_mri.all():
            total = total+service.fee
        return total

class CT_Invoice (models.Model):
    class Meta:
        verbose_name = "Invoice (CT-Scan)"
        verbose_name_plural = 'Invoices (Ct-Scan)'

    date = models.DateField(verbose_name="reception date", auto_now=False, auto_now_add=False)
    time = models.TimeField(verbose_name="reception time", auto_now=False, auto_now_add=False)
    Patient = models.ForeignKey(Patient, verbose_name="patient", on_delete=models.CASCADE)
    RefferalPhysician = models.ForeignKey(ReferralPhysician, verbose_name='refferal physician', on_delete=models.CASCADE,null=True,blank=True)
    services_ctscan = models.ManyToManyField(ServiceCtscan,blank=True ,related_name="ct_service")
    discount = models.DecimalField(verbose_name='discount', max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return str(self.id)+" "+ str(self.date)+(self.Patient.first_name)

    def patient_name(self):
        return str(self.Patient)
    
    def total_fee(self):
        total = 0
        for service in self.services_ctscan.all():
            total = total+service.fee
        return total


class X_Ray_Invoice (models.Model):
    class Meta:
        verbose_name = "Invoice (X-ray)"
        verbose_name_plural = 'Invoices (X-ray)'

    date = models.DateField(verbose_name="reception date", auto_now=False, auto_now_add=False)
    time = models.TimeField(verbose_name="reception time", auto_now=False, auto_now_add=False)
    Patient = models.ForeignKey(Patient, verbose_name="patient", on_delete=models.CASCADE)
    RefferalPhysician = models.ForeignKey(ReferralPhysician, verbose_name='refferal physician', on_delete=models.CASCADE,null=True,blank=True)
    services_xray = models.ManyToManyField(ServiceXray,blank=True, related_name='x_invoice')
    discount = models.DecimalField(verbose_name='discount', max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return str(self.id)+" "+ str(self.date)+(self.Patient.first_name)

    def patient_name(self):
        return str(self.Patient)
    
    def total_fee(self):
        total = 0
        for service in self.services_xray.all():
            total = total+service.fee
        return total

        
class Expenses (models.Model):
    name = models.CharField(verbose_name="expense name",max_length=150)
    cost = models.DecimalField(verbose_name="cost", max_digits=8, decimal_places=2)
    quantity = models.IntegerField(verbose_name="quantity")
    date = models.DateField(verbose_name="date",auto_now=False, auto_now_add=False)