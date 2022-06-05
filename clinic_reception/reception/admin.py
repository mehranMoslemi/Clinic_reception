from django.utils.html import format_html
from django.contrib import admin
from .models import Patient , ReferralPhysician , Physician , Invoice , ServiceMri , ServiceCtscan, ServiceXray , Expenses



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

class InvoiceAdmin(admin.ModelAdmin):
    def print_mri(self, obj):
        return format_html('<a class="btn btn-danger" target="_blank" href="/reception/invoice/{}/mri">Print MRI</a>', obj.id)

    def print_ct_scan(self, obj):
        return format_html('<a class="btn btn-danger" target="_blank" href="/reception/invoice/{}/ct">Print CT scan</a>', obj.id)

    def print_x_ray(self, obj):
        return format_html('<a class="btn btn-danger" target="_blank" href="/reception/invoice/{}/xray">Print X-ray</a>', obj.id)

    list_display = ('code','date','print_mri','print_ct_scan','print_x_ray')

class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('name','cost','quantity','date')

admin.site.register(Patient,PatientAdmin)
admin.site.register(ReferralPhysician,ReferralPhysicianAdmin)
admin.site.register(Physician,PhysicianAdmin)
admin.site.register(ServiceCtscan,ServiceCtscanAdmin)
admin.site.register(ServiceMri,ServiceMriAdmin)
admin.site.register(ServiceXray,ServiceXrayAdmin)
admin.site.register(Invoice,InvoiceAdmin)
admin.site.register(Expenses,ExpensesAdmin)