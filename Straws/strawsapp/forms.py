from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import WorkersDetail,TableForm1,TableForm2,TableForm3

class worker_signup_form(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class TableModelForm1(forms.ModelForm):

    class Meta:
        model = TableForm1
        fields = '__all__'

class TableModelForm2(forms.ModelForm):

    class Meta:
        model = TableForm2
        fields = '__all__'

class TableModelForm3(forms.ModelForm):

    class Meta:
        model = TableForm3
        fields = '__all__'