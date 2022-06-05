
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum
from .models import Invoice , Patient,ReferralPhysician
def invoice(request,id , type):
    if type == 'mri':
        invoice = Invoice.objects.get(pk=id)
        patient = Patient.objects.filter(invoice =invoice).all()[0]
        mri_service = invoice.services_mri.all()
        total_mri = invoice.services_mri.aggregate(Sum('fee')).get('fee__sum')
        total_ct = invoice.services_ctscan.aggregate(Sum('fee')).get('fee__sum')
        total_xray = invoice.services_xray.aggregate(Sum('fee')).get('fee__sum')
        ref_fee = ReferralPhysician.objects.filter(invoice = invoice).aggregate(Sum('fee')).get('fee__sum')

        if total_mri is None:
            return HttpResponse("<h1>this patient has no mri service registered in invoice!</h1>")
        if total_ct is None:
            total_ct = 0
        if total_xray is None:
            total_xray = 0
        if ref_fee is None:
            ref_fee = 0
        other_total = total_ct+total_xray
        total = total_ct+total_xray+total_mri+ref_fee
        context = {
            'code':invoice.code,
            'date':invoice.date,
            'p_name':patient.first_name,
            'p_midname':patient.middle_name,
            'p_lastname':patient.last_name,
            'p_bdate':patient.date_of_birth,
            'p_gender':patient.gender,
            'p_phone':patient.phone,
            'services':mri_service,
            'ref_fee' :float(ref_fee),
            'service_fee':float(total_mri),
            'other_fee':float(other_total),
            'total':float(total)}
        return render(request , 'reception/invoice.html',context=context)
    elif type == 'ct':
        invoice = Invoice.objects.get(pk=id)
        patient = Patient.objects.filter(invoice =invoice).all()[0]
        ctscan_service = invoice.services_ctscan.all()
        total_mri = invoice.services_mri.aggregate(Sum('fee')).get('fee__sum')
        total_ct = invoice.services_ctscan.aggregate(Sum('fee')).get('fee__sum')
        total_xray = invoice.services_xray.aggregate(Sum('fee')).get('fee__sum')
        ref_fee = ReferralPhysician.objects.filter(invoice = invoice).aggregate(Sum('fee')).get('fee__sum')

        if total_ct is None:
            return HttpResponse("<h1>this patient has no ct_scan service registered in invoice!</h1>")
        if total_mri is None:
            total_mri = 0
        if total_xray is None:
            total_xray = 0
        if ref_fee is None:
            ref_fee = 0
        other_total = total_mri+total_xray
        total = total_ct+total_xray+total_mri+ref_fee
        context = {
            'code':invoice.code,
            'date':invoice.date,
            'p_name':patient.first_name,
            'p_midname':patient.middle_name,
            'p_lastname':patient.last_name,
            'p_bdate':patient.date_of_birth,
            'p_gender':patient.gender,
            'p_phone':patient.phone,
            'services':ctscan_service,
            'ref_fee' :float(ref_fee),
            'service_fee':float(total_ct),
            'other_fee':float(other_total),
            'total':float(total)}
        return render(request , 'reception/invoice.html',context=context)

    elif type == 'xray':
        invoice = Invoice.objects.get(pk=id)
        patient = Patient.objects.filter(invoice =invoice).all()[0]
        xray_service = invoice.services_xray.all()
        total_mri = invoice.services_mri.aggregate(Sum('fee')).get('fee__sum')
        total_ct = invoice.services_ctscan.aggregate(Sum('fee')).get('fee__sum')
        total_xray = invoice.services_xray.aggregate(Sum('fee')).get('fee__sum')
        ref_fee = ReferralPhysician.objects.filter(invoice = invoice).aggregate(Sum('fee')).get('fee__sum')

        if total_xray is None:
            return HttpResponse("<h1>this patient has no X-ray service registered in invoice!</h1>")
        if total_mri is None:
            total_mri = 0
        if total_ct is None:
            total_ct = 0
        if ref_fee is None:
            ref_fee = 0
        other_total = total_mri+total_ct
        total = total_ct+total_xray+total_mri+ref_fee
        context = {
            'code':invoice.code,
            'date':invoice.date,
            'p_name':patient.first_name,
            'p_midname':patient.middle_name,
            'p_lastname':patient.last_name,
            'p_bdate':patient.date_of_birth,
            'p_gender':patient.gender,
            'p_phone':patient.phone,
            'services':xray_service,
            'ref_fee' :float(ref_fee),
            'service_fee':float(total_xray),
            'other_fee':float(other_total),
            'total':float(total)}
        return render(request , 'reception/invoice.html',context=context)