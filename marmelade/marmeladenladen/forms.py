from django import forms

class UserForm(forms.Form):
    f_decision1= forms.CharField(max_length=100)
    f_decision2= forms.CharField(max_length=100)
    f_decision3= forms.CharField(max_length=100)
    s_decision= forms.CharField(max_length=100)
