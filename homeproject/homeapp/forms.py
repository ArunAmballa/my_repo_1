from django import forms

class HomeForm(forms.Form):
    name=forms.CharField()

class AgeForm(forms.Form):
    age=forms.IntegerField()

class MarksForm(forms.Form):
    marks=forms.IntegerField()
