from django import forms

g=[('male','MALE'),('female','FEMALE')]
class SignupForm(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    gender=forms.ChoiceField(choices=g)
