
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum
from .models import CT_Invoice, Mri_Invoice , Patient,ReferralPhysician, X_Ray_Invoice
def invoice(request,id , type):
    if type == 'mri':
        invoice = Mri_Invoice.objects.get(pk=id)
        patient = Patient.objects.filter(mri_invoice =invoice).all()[0]
        mri_service = invoice.services_mri.all()
        total_mri = invoice.services_mri.aggregate(Sum('fee')).get('fee__sum')
        ref_fee = ReferralPhysician.objects.filter(mri_invoice = invoice).aggregate(Sum('fee')).get('fee__sum')

        if total_mri is None:
            return HttpResponse("<h1>this patient has no ct_scan service registered in invoice!</h1>")
       
        if ref_fee is None:
            ref_fee = 0
            
        other_total = ref_fee
        context = {
            'code':invoice.id,
            'date':invoice.date,
            'p_name':patient.first_name,
            'p_midname':patient.middle_name,
            'p_lastname':patient.last_name,
            'p_bdate':patient.date_of_birth,
            'p_gender':patient.gender,
            'p_phone':patient.phone,
            'services':mri_service,
            'discount' :float(invoice.discount),
            'service_fee':float(total_mri),
            'other_fee':float(other_total),
            'total':float(total_mri+other_total-invoice.discount)}
        return render(request , 'reception/invoice.html',context=context)
    
    elif type == 'ct':
        invoice = CT_Invoice.objects.get(pk=id)
        patient = Patient.objects.filter(ct_invoice =invoice).all()[0]
        ctscan_service = invoice.services_ctscan.all()
        total_ct = invoice.services_ctscan.aggregate(Sum('fee')).get('fee__sum')
        ref_fee = ReferralPhysician.objects.filter(ct_invoice = invoice).aggregate(Sum('fee')).get('fee__sum')

        if total_ct is None:
            return HttpResponse("<h1>this patient has no ct_scan service registered in invoice!</h1>")
       
        if ref_fee is None:
            ref_fee = 0
            
        other_total = ref_fee
        context = {
            'code':invoice.id,
            'date':invoice.date,
            'p_name':patient.first_name,
            'p_midname':patient.middle_name,
            'p_lastname':patient.last_name,
            'p_bdate':patient.date_of_birth,
            'p_gender':patient.gender,
            'p_phone':patient.phone,
            'services':ctscan_service,
            'discount' :float(invoice.discount),
            'service_fee':float(total_ct),
            'other_fee':float(other_total),
            'total':float(total_ct+other_total-invoice.discount)}
        return render(request , 'reception/invoice.html',context=context)

    elif type == 'xray':
        invoice = X_Ray_Invoice.objects.get(pk=id)
        patient = Patient.objects.filter(x_ray_invoice =invoice).all()[0]
        xray_service = invoice.services_xray.all()
        total_xray = invoice.services_xray.aggregate(Sum('fee')).get('fee__sum')
        ref_fee = ReferralPhysician.objects.filter(x_ray_invoice = invoice).aggregate(Sum('fee')).get('fee__sum')

        if total_xray is None:
            return HttpResponse("<h1>this patient has no ct_scan service registered in invoice!</h1>")
       
        if ref_fee is None:
            ref_fee = 0
            
        other_total = ref_fee
        context = {
            'code':invoice.id,
            'date':invoice.date,
            'p_name':patient.first_name,
            'p_midname':patient.middle_name,
            'p_lastname':patient.last_name,
            'p_bdate':patient.date_of_birth,
            'p_gender':patient.gender,
            'p_phone':patient.phone,
            'services':xray_service,
            'discount' :float(invoice.discount),
            'service_fee':float(total_xray),
            'other_fee':float(other_total),
            'total':float(total_xray+other_total-invoice.discount)}
        return render(request , 'reception/invoice.html',context=context)