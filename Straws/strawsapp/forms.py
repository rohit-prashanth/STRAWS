from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import WorkersDetail

class worker_signup_form(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','email']