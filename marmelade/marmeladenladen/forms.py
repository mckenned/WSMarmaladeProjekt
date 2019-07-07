from django import forms

class SelectionForm(forms.Form):
    decision= forms.CharField()
    #decision2= forms.CharField()

'''
    def __init__(self):
        if check_something():
            self.fields['decision'].initial  = False
'''
