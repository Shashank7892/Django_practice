from django import forms

class UserForm(forms.Form):
    num1=forms.IntegerField(label="value 1",required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    num2=forms.IntegerField(label="value 2",required=False,widget=forms.TextInput(attrs={'class':'form-control'}))