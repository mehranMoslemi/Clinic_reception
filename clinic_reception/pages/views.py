
from calendar import day_abbr, month
import datetime
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from numpy import empty
from .forms import DateForm
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
            date = item.date
            discount = item.discount
            data.append({'date':date,'mri':mri_tot,'discount':discount})
        dt = pd.DataFrame(data)
        g_list = dt.groupby(['date']).agg(sum)
        passlist=[]
        for index, row in g_list.iterrows():
            passlist.append({'dt':index,'mri':row[0],'discount':row[1] ,'total': float(row[0])-float(row[1]),'day':index.day})
        context = {'values':passlist}
        print(passlist)
        return render(request , 'pages/index.html',context)

@login_required(login_url='login')
def report_expanses(request):
    if is_super:
        items = Expenses.objects.filter(date__lte=datetime.datetime.today(), date__gt=datetime.datetime.today()-datetime.timedelta(days=30))
        data = []
        for item in items:
            cost_tot= item.quantity * item.cost
            data.append({'date':item.date,'cost':cost_tot})
        dt = pd.DataFrame(data)
        passlist =[]
        g_list = dt.groupby(['date']).agg(sum)
        for index, row in g_list.iterrows():
            passlist.append({'dt':index,'exp':row[0],'day':index.day})
        context = {'values': passlist}
        print(passlist)
        return render(request , 'pages/repexpenses.html',context)

@login_required(login_url='login')
def report_patient_count_mri(request):
    if is_super:
        items = Mri_Invoice.objects.filter(date__lte=datetime.datetime.today(), date__gt=datetime.datetime.today()-datetime.timedelta(days=30))
        data = []
        for item in items:
            mri_tot = item.services_mri.aggregate(Count('id')).get('id__count')
            date = item.date
            data.append({'date':date,'mri':mri_tot})
        dt = pd.DataFrame(data)
        g_list = dt.groupby(['date']).agg(sum)
        passlist=[]
        for index, row in g_list.iterrows():
            passlist.append({'dt':index,'service':row[0],'day':index.day})
        context = {'values':passlist,'label':'MRI'}
        print(passlist)
        return render(request , 'pages/p_count_rep.html',context)

@login_required(login_url='login')
def report_patient_count_ct(request):
    if is_super:
        items = CT_Invoice.objects.filter(date__lte=datetime.datetime.today(), date__gt=datetime.datetime.today()-datetime.timedelta(days=30))
        data = []
        for item in items:
            ct_tot = item.services_ctscan.aggregate(Count('id')).get('id__count')
            date = item.date
            data.append({'date':date,'ct':ct_tot})
        dt = pd.DataFrame(data)
        g_list = dt.groupby(['date']).agg(sum)
        passlist=[]
        for index, row in g_list.iterrows():
            passlist.append({'dt':index,'service':row[0],'day':index.day})
        context = {'values':passlist,'label':'CT_Scan'}
        print(passlist)
        return render(request , 'pages/p_count_rep.html',context)

@login_required(login_url='login')
def report_patient_count_x_ray(request):
    if is_super:
        items = X_Ray_Invoice.objects.filter(date__lte=datetime.datetime.today(), date__gt=datetime.datetime.today()-datetime.timedelta(days=30))
        data = []
        for item in items:
            x_tot = item.services_xray.aggregate(Count('id')).get('id__count')
            date = item.date
            data.append({'date':date,'x':x_tot})
        dt = pd.DataFrame(data)
        g_list = dt.groupby(['date']).agg(sum)
        passlist=[]
        for index, row in g_list.iterrows():
            passlist.append({'dt':index,'service':row[0],'day':index.day})
        context = {'values':passlist,'label':'X_ray'}
        print(passlist)
        return render(request , 'pages/p_count_rep.html',context)

@login_required(login_url='login')
def income_mri(request):
    if is_super:
        items = Mri_Invoice.objects.filter(date__lte=datetime.datetime.today(), date__gt=datetime.datetime.today()-datetime.timedelta(days=30))
        data = []
        for item in items:
            mri_tot = item.services_mri.aggregate(Sum('fee')).get('fee__sum')
            date = item.date
            discount = item.discount
            data.append({'date':date,'mri':mri_tot,'discount':discount})
        dt = pd.DataFrame(data)
        g_list = dt.groupby(['date']).agg(sum)
        passlist=[]
        for index, row in g_list.iterrows():
            passlist.append({'dt':index,'service':row[0],'discount':row[1] ,'total': float(row[0])-float(row[1]),'day':index.day})
        context = {'values':passlist,'label':'MRI'}
        print(passlist)
        return render(request , 'pages/income.html',context)

@login_required(login_url='login')
def income_ct(request):
    if is_super:
        items = CT_Invoice.objects.filter(date__lte=datetime.datetime.today(), date__gt=datetime.datetime.today()-datetime.timedelta(days=30))
        data = []
        for item in items:
            ct_tot = item.services_ctscan.aggregate(Sum('fee')).get('fee__sum')
            date = item.date
            discount = item.discount
            data.append({'date':date,'ct':ct_tot,'discount':discount})
        dt = pd.DataFrame(data)
        g_list = dt.groupby(['date']).agg(sum)
        passlist=[]
        for index, row in g_list.iterrows():
            passlist.append({'dt':index,'service':row[0],'discount':row[1] ,'total': float(row[0])-float(row[1]),'day':index.day})
        context = {'values':passlist,'label':'CT Scan'}
        print(passlist)
        return render(request , 'pages/income.html',context)

@login_required(login_url='login')
def income_x(request):
    if is_super:
        items = X_Ray_Invoice.objects.filter(date__lte=datetime.datetime.today(), date__gt=datetime.datetime.today()-datetime.timedelta(days=30))
        data = []
        for item in items:
            x_tot = item.services_xray.aggregate(Sum('fee')).get('fee__sum')
            date = item.date
            discount = item.discount
            data.append({'date':date,'x':x_tot,'discount':discount})
        dt = pd.DataFrame(data)
        g_list = dt.groupby(['date']).agg(sum)
        passlist=[]
        for index, row in g_list.iterrows():
            passlist.append({'dt':index,'service':row[0],'discount':row[1] ,'total': float(row[0])-float(row[1]),'day':index.day})
        context = {'values':passlist,'label':'X Ray'}
        print(passlist)
        return render(request , 'pages/income.html',context)

@login_required(login_url='login')
def report_refferal_mri(request):
    if is_super:
        items = Mri_Invoice.objects.filter(date__lte=datetime.datetime.today(), date__gt=datetime.datetime.today()-datetime.timedelta(days=30))
        reflist = []
        for item in items:
            if item.RefferalPhysician is not None:
                reflist.append({'date':item.date , "name":item.RefferalPhysician.first_name+" "+item.RefferalPhysician.last_name , 'fee':item.RefferalPhysician.fee})
        
        df = pd.DataFrame(reflist)
        g_list = df.groupby(['date','name']).agg(sum)
        passlist=[]
        
        for index, row in g_list.iterrows():
            passlist.append({'dt':index[0],'name':index[1],'fee':row[0],'day':index[0].day})

        context = {'values':passlist}
        print(passlist)
        return render(request , 'pages/refferal.html',context)

@login_required(login_url='login')
def report_refferal_ct(request):
    if is_super:
        items = CT_Invoice.objects.filter(date__lte=datetime.datetime.today(), date__gt=datetime.datetime.today()-datetime.timedelta(days=30))
        reflist = []
        for item in items:
            if item.RefferalPhysician is not None:
                reflist.append({'date':item.date , "name":item.RefferalPhysician.first_name+" "+item.RefferalPhysician.last_name , 'fee':item.RefferalPhysician.fee})
        
        df = pd.DataFrame(reflist)
        g_list = df.groupby(['date','name']).agg(sum)
        passlist=[]
        
        for index, row in g_list.iterrows():
            passlist.append({'dt':index[0],'name':index[1],'fee':row[0],'day':index[0].day})

        context = {'values':passlist}
        print(passlist)
        return render(request , 'pages/refferal.html',context)

@login_required(login_url='login')
def report_refferal_x_ray(request):
    if is_super:
        items = X_Ray_Invoice.objects.filter(date__lte=datetime.datetime.today(), date__gt=datetime.datetime.today()-datetime.timedelta(days=30))
        reflist = []
        for item in items:
            if item.RefferalPhysician is not None:
                reflist.append({'date':item.date , "name":item.RefferalPhysician.first_name+" "+item.RefferalPhysician.last_name , 'fee':item.RefferalPhysician.fee})
        
        df = pd.DataFrame(reflist)
        g_list = df.groupby(['date','name']).agg(sum)
        passlist=[]
        
        for index, row in g_list.iterrows():
            passlist.append({'dt':index[0],'name':index[1],'fee':row[0],'day':index[0].day})

        context = {'values':passlist}
        print(passlist)
        return render(request , 'pages/refferal.html',context)

@login_required(login_url='login')
def date_report(request,type):
    if request.method == 'POST':
        form= DateForm(request.POST or None)
        if form.is_valid():
            date_to = form.cleaned_data.get("date_to")
            date_from = form.cleaned_data.get("date_from")
            if type =='MRI':
                invoices = Mri_Invoice.objects.filter(date__range=[date_from,date_to])
            elif type == 'CT_SCAN':
                invoices = CT_Invoice.objects.filter(date__range=[date_from,date_to])
            else :
                invoices = X_Ray_Invoice.objects.filter(date__range=[date_from,date_to])
            print('invoice count = ',invoices.count())
            print_list = list()
            grand_total = 0.0
            grand_discount = 0.0
            for invoice in invoices:
                if type =="MRI":
                    services = invoice.services_mri.all()
                elif type =="CT_SCAN":
                    services = invoice.services_ctscan.all()
                else:
                    services = invoice.services_xray.all()
                for service in services:
                    print_list.append({'id':invoice.id,'date':invoice.date,'patient_name':invoice.patient_name(),'doc':service.physician,'ex_fee':service.fee,'discount':invoice.discount/services.count(),'total':service.fee-invoice.discount/services.count()})
                    grand_total += float(service.fee-invoice.discount/services.count())
                    grand_discount += float(invoice.discount/services.count())
            return render(request,'pages/report_table.html',context={'form':form,'print_list':print_list,'type':type,'gt':grand_total,'gd':grand_discount,'dt':date_to,'df':date_from})
        else:
            return render(request,'pages/date_picker_table.html',context={'form':form})
        
    else:
        form= DateForm(request.POST or None)
        return render(request,'pages/date_picker_table.html',context={'form':form})
