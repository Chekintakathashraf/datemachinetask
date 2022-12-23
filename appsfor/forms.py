from django import forms

class DateRangeForm(forms.Form):
    startingdate = forms.DateField()
    endingdate = forms.DateField()
    