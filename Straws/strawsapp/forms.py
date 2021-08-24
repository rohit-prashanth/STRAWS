from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import WorkersDetail,TableForm1,TableForm2,TableForm3,TableForm4,TableForm5,TableForm6,TableForm7,TableForm8,TableForm9,TableForm10

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

class TableModelForm4(forms.ModelForm):

    class Meta:
        model = TableForm4
        fields = '__all__'

class TableModelForm5(forms.ModelForm):

    class Meta:
        model = TableForm5
        fields = '__all__'

class TableModelForm6(forms.ModelForm):

    class Meta:
        model = TableForm6
        fields = '__all__'

class TableModelForm7(forms.ModelForm):

    class Meta:
        model = TableForm7
        fields = '__all__'

class TableModelForm8(forms.ModelForm):

    class Meta:
        model = TableForm8
        fields = '__all__'

class TableModelForm9(forms.ModelForm):

    class Meta:
        model = TableForm9
        fields = '__all__'

class TableModelForm10(forms.ModelForm):

    class Meta:
        model = TableForm10
        fields = '__all__'