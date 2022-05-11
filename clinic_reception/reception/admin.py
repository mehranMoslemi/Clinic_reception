from django.contrib import admin
from .models import Patient , RefferalPhysician , Physician , Invoice , ServiceMri , ServiceCtscan, ServiceXray , Expenses



class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','code','date_of_birth')
    list_filter = ('first_name', 'last_name', 'code')
    search_fields =('code','first_name','last_name')


admin.site.register(Patient,PatientAdmin)
admin.site.register(RefferalPhysician)
admin.site.register(Physician)
admin.site.register(ServiceCtscan)
admin.site.register(ServiceMri)
admin.site.register(ServiceXray)
admin.site.register(Invoice)
admin.site.register(Expenses)