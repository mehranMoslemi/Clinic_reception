from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path('mri-p-count',views.report_patient_count_mri,name ='mri_p_count'),
    path('ct-p-count',views.report_patient_count_ct,name ='ct_p_count'),
    path('x-p-count',views.report_patient_count_x_ray,name ='x_p_count'),

    path('mri_income',views.income_mri,name ='mri_income'),
    path('ct_income',views.income_ct,name ='ct_income'),
    path('x_income',views.income_x,name ='x_income'),

    path('report-referral_mri',views.report_refferal_mri,name='mri_ref'),
    path('report-referral_ct',views.report_refferal_ct,name='ct_ref'),
    path('report-referral_x',views.report_refferal_x_ray,name='x_ref'),

    path('report-expenses',views.report_expanses,name='rexp'),
]
