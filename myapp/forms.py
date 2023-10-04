from django import forms
from .models import Studentdetail

class StudentdetailForm(forms.ModelForm):
    class Meta:
        model = Studentdetail
        fields = ['name', 'phone_number', 'dob', 'nationality', 'email', 'institute', 'blood_group']
