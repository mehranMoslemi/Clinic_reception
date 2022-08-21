from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput

class DateForm(forms.Form):
    date_from = forms.DateTimeField(widget=DatePickerInput())
    date_to= forms.DateTimeField(widget=DatePickerInput())
    