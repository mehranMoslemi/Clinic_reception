
import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from numpy import empty
from reception.forms import PatientForm
from reception.models import CT_Invoice,Mri_Invoice,X_Ray_Invoice,Expenses
from django.db.models import Count , Sum
import pandas as pd

def is_super(request):
    if request.user.is_superuser:
        return True
    else:
        return redirect('admin/')

@login_required(login_url='login')
def index(request):
    if is_super:
        items = Mri_Invoice.objects.filter(date__lte=datetime.datetime.today(), date__gt=datetime.datetime.today()-datetime.timedelta(days=30))
        data = []
        for item in items:
            mri_tot = item.services_mri.aggregate(Sum('fee')).get('fee__sum')
            ct_tot = item.services_ctscan.aggregate(Sum('fee')).get('fee__sum')
            x_tot = item.services_xray.aggregate(Sum('fee')).get('fee__sum')
            date = item.date
            data.append({'date':date,'mri':mri_tot,'ct':ct_tot,'x':x_tot})
        dt = pd.DataFrame(data)
        if dt.size>0:
            g_list = dt.groupby(['date']).agg(sum)
            passlist=[]
            for index, row in g_list.iterrows():
                passlist.append({'dt':index,'mri':row[0],'ct':row[1],'x':row[2],'day':index.day})
            context = {'values':passlist}
            print(passlist)
            return render(request , 'pages/index.html',context)
        else:
            return render(request, 'pages/index.html')


# @login_required(login_url='login')
# def patient(request):
#     form = PatientForm()
#     context = {'form':form}
#     return render(request , 'pages/patient.html',context)

# @login_required(login_url='login')
# def report_mnt(request):
#     if is_super:
#         items = Invoice.objects.filter(date__lte=datetime.datetime.today(), date__gt=datetime.datetime.today()-datetime.timedelta(days=30))
#         data = []
#         for item in items:
#             mri_tot = item.services_mri.aggregate(Sum('fee')).get('fee__sum')
#             ct_tot = item.services_ctscan.aggregate(Sum('fee')).get('fee__sum')
#             x_tot = item.services_xray.aggregate(Sum('fee')).get('fee__sum')
#             date = item.date
#             data.append({'date':date,'mri':mri_tot,'ct':ct_tot,'x':x_tot})
#         dt = pd.DataFrame(data)
#         g_list = dt.groupby(['date']).agg(sum)
#         passlist=[]
#         for index, row in g_list.iterrows():
#             passlist.append({'dt':index,'mri':row[0],'ct':row[1],'x':row[2],'day':index.day})
#         context = {'values':passlist}
#         print(passlist)
#         return render(request , 'pages/reportmnt.html',context)


# @login_required(login_url='login')
# def report_expanses(request):
#     if is_super:
#         items = Expenses.objects.filter(date__lte=datetime.datetime.today(), date__gt=datetime.datetime.today()-datetime.timedelta(days=30))
#         data = []
#         for item in items:
#             cost_tot= item.quantity * item.cost
#             data.append({'date':item.date,'cost':cost_tot})
#         dt = pd.DataFrame(data)
#         passlist =[]
#         g_list = dt.groupby(['date']).agg(sum)
#         for index, row in g_list.iterrows():
#             passlist.append({'dt':index,'exp':row[0],'day':index.day})
#         context = {'values': passlist}
#         print(passlist)
#         return render(request , 'pages/repexpenses.html',context)

# @login_required(login_url='login')
# def report_patient_count(request):
#     if is_super:
#         items = Invoice.objects.filter(date__lte=datetime.datetime.today(), date__gt=datetime.datetime.today()-datetime.timedelta(days=30))
#         data = []
#         for item in items:
#             mri_tot = item.services_mri.aggregate(Count('id')).get('id__count')
#             ct_tot = item.services_ctscan.aggregate(Count('id')).get('id__count')
#             x_tot = item.services_xray.aggregate(Count('id')).get('id__count')
#             date = item.date
#             data.append({'date':date,'mri':mri_tot,'ct':ct_tot,'x':x_tot})
#         dt = pd.DataFrame(data)
#         g_list = dt.groupby(['date']).agg(sum)
#         passlist=[]
#         for index, row in g_list.iterrows():
#             passlist.append({'dt':index,'mri':row[0],'ct':row[1],'x':row[2],'day':index.day})
#         context = {'values':passlist}
#         print(passlist)
#         return render(request , 'pages/reportmnt.html',context)

# @login_required(login_url='login')
# def report_refferal(request):
#     if is_super:
#         items = Invoice.objects.filter(date__lte=datetime.datetime.today(), date__gt=datetime.datetime.today()-datetime.timedelta(days=30))
#         reflist = []
#         for item in items:
#             if item.RefferalPhysician is not None:
#                 reflist.append({'date':item.date , "name":item.RefferalPhysician.first_name+" "+item.RefferalPhysician.last_name , 'fee':item.RefferalPhysician.fee})
        
#         df = pd.DataFrame(reflist)
#         g_list = df.groupby(['date','name']).agg(sum)
#         passlist=[]
        
#         for index, row in g_list.iterrows():
#             passlist.append({'dt':index[0],'name':index[1],'fee':row[0],'day':index[0].day})

#         context = {'values':passlist}
#         print(passlist)
#         return render(request , 'pages/refferal.html',context)