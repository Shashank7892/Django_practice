from django import forms

class evenoddform(forms.Form):
    num=forms.IntegerField(label="Value 1")
    