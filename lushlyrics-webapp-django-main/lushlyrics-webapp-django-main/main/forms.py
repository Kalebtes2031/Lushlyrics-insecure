# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    
    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'phone_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['full_name'].split(' ')[0]
        user.last_name = ' '.join(self.cleaned_data['full_name'].split(' ')[1:])
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user
    
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, required= True, widget=forms.EmailInput(attrs={'class':'form-control'}))

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

