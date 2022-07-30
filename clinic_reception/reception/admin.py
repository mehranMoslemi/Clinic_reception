from django.utils.html import format_html
from django.contrib import admin
from .models import CT_Invoice, Mri_Invoice, Patient , ReferralPhysician , Physician  , ServiceMri , ServiceCtscan, ServiceXray , Expenses, X_Ray_Invoice



class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','code','date_of_birth')
    list_filter = ('first_name', 'last_name', 'code')
    search_fields =('code','first_name','last_name')

class ReferralPhysicianAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','field','fee')

class PhysicianAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','field')

class ServiceCtscanAdmin(admin.ModelAdmin):
    list_display = ('name','physician','fee')

class ServiceMriAdmin(admin.ModelAdmin):
    list_display = ('name','physician','fee')

class ServiceXrayAdmin(admin.ModelAdmin):
    list_display = ('name','physician','fee')

class MRI_InvoiceAdmin(admin.ModelAdmin):
    def print_mri(self, obj):
        return format_html('<a class="btn btn-danger" target="_blank" href="/reception/invoice/{}/mri">Print MRI invoice</a>', obj.id)

    list_display = ('id','date','print_mri')

class CT_InvoiceAdmin(admin.ModelAdmin):
    def print_ct(self, obj):
        return format_html('<a class="btn btn-danger" target="_blank" href="/reception/invoice/{}/ct">Print CT_Scan invoice</a>', obj.id)

    list_display = ('id','date','print_ct')

class X_Ray_InvoiceAdmin(admin.ModelAdmin):
    def print_x(self, obj):
        return format_html('<a target="_blank" href="/reception/invoice/{}/xray">Print X_ray invoice</a>', obj.id)

    list_display = ('id','date','print_x')

class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('name','cost','quantity','date')

admin.site.register(Patient,PatientAdmin)
admin.site.register(ReferralPhysician,ReferralPhysicianAdmin)
admin.site.register(Physician,PhysicianAdmin)
admin.site.register(ServiceCtscan,ServiceCtscanAdmin)
admin.site.register(ServiceMri,ServiceMriAdmin)
admin.site.register(ServiceXray,ServiceXrayAdmin)
admin.site.register(Mri_Invoice,MRI_InvoiceAdmin)
admin.site.register(CT_Invoice,CT_InvoiceAdmin)
admin.site.register(X_Ray_Invoice,X_Ray_InvoiceAdmin)
admin.site.register(Expenses,ExpensesAdmin)