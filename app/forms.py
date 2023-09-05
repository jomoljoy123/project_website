from django import forms
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email=forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    confirm_password = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=100)
    date_of_birth = forms.IntegerField
    district = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    pincode = forms.IntegerField
    upload_image=forms.ImageField()