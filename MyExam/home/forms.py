from django import forms

class doTestForm(forms.Form):
    CHOICES = [('M','Male'),('F','Female')]
    aa=forms.CharField()