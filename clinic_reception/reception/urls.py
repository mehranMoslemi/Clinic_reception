from django.urls import path
from .import views

urlpatterns = [
    path('invoice/<int:id>/<str:type>',views.invoice,name="invoice")
]
