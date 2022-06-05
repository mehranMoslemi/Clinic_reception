from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from reception.forms import PatientForm

@login_required(login_url='login')
def index(request):
    return render(request , 'pages/index.html')


@login_required(login_url='login')
def patient(request):
    form = PatientForm()
    context = {'form':form}
    return render(request , 'pages/patient.html',context)