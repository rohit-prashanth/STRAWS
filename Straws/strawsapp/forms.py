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
        mode_choice = [('Cash', 'Cash'), ('UPI', 'UPI'), ('Card Payment', 'Card Payment')]
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Name'}),
        'mobile_number': forms.TextInput(attrs={'class': 'form-control' }),
        'items': forms.Textarea(attrs={'class': 'form-control' }),
        'total_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        'payment_mode': forms.Select(attrs={'class': 'form-control','choices':mode_choice})
        }

class TableModelForm2(forms.ModelForm):

    class Meta:
        model = TableForm2
        fields = '__all__'
        mode_choice = [('Cash', 'Cash'), ('UPI', 'UPI'), ('Card Payment', 'Card Payment')]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Name'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'items': forms.Textarea(attrs={'class': 'form-control'}),
            'total_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_mode': forms.Select(attrs={'class': 'form-control', 'choices': mode_choice})
        }

class TableModelForm3(forms.ModelForm):

    class Meta:
        model = TableForm3
        fields = '__all__'
        mode_choice = [('Cash', 'Cash'), ('UPI', 'UPI'), ('Card Payment', 'Card Payment')]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Name'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'items': forms.Textarea(attrs={'class': 'form-control'}),
            'total_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_mode': forms.Select(attrs={'class': 'form-control', 'choices': mode_choice})
        }

class TableModelForm4(forms.ModelForm):

    class Meta:
        model = TableForm4
        fields = '__all__'
        mode_choice = [('Cash', 'Cash'), ('UPI', 'UPI'), ('Card Payment', 'Card Payment')]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Name'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'items': forms.Textarea(attrs={'class': 'form-control'}),
            'total_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_mode': forms.Select(attrs={'class': 'form-control', 'choices': mode_choice})
        }

class TableModelForm5(forms.ModelForm):

    class Meta:
        model = TableForm5
        fields = '__all__'
        mode_choice = [('Cash', 'Cash'), ('UPI', 'UPI'), ('Card Payment', 'Card Payment')]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Name'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'items': forms.Textarea(attrs={'class': 'form-control'}),
            'total_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_mode': forms.Select(attrs={'class': 'form-control', 'choices': mode_choice})
        }

class TableModelForm6(forms.ModelForm):

    class Meta:
        model = TableForm6
        fields = '__all__'
        mode_choice = [('Cash', 'Cash'), ('UPI', 'UPI'), ('Card Payment', 'Card Payment')]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Name'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'items': forms.Textarea(attrs={'class': 'form-control'}),
            'total_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_mode': forms.Select(attrs={'class': 'form-control', 'choices': mode_choice})
        }

class TableModelForm7(forms.ModelForm):

    class Meta:
        model = TableForm7
        fields = '__all__'
        mode_choice = [('Cash', 'Cash'), ('UPI', 'UPI'), ('Card Payment', 'Card Payment')]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer name'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'items': forms.Textarea(attrs={'class': 'form-control'}),
            'total_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_mode': forms.Select(attrs={'class': 'form-control', 'choices': mode_choice})
        }

class TableModelForm8(forms.ModelForm):

    class Meta:
        model = TableForm8
        fields = '__all__'
        mode_choice = [('Cash', 'Cash'), ('UPI', 'UPI'), ('Card Payment', 'Card Payment')]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Name'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'items': forms.Textarea(attrs={'class': 'form-control'}),
            'total_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_mode': forms.Select(attrs={'class': 'form-control', 'choices': mode_choice})
        }

class TableModelForm9(forms.ModelForm):

    class Meta:
        model = TableForm9
        fields = '__all__'
        mode_choice = [('Cash', 'Cash'), ('UPI', 'UPI'), ('Card Payment', 'Card Payment')]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Name'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'items': forms.Textarea(attrs={'class': 'form-control'}),
            'total_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_mode': forms.Select(attrs={'class': 'form-control', 'choices': mode_choice})
        }

class TableModelForm10(forms.ModelForm):

    class Meta:
        model = TableForm10
        fields = '__all__'
        mode_choice = [('Cash', 'Cash'), ('UPI', 'UPI'), ('Card Payment', 'Card Payment')]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Name'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'items': forms.Textarea(attrs={'class': 'form-control'}),
            'total_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_mode': forms.Select(attrs={'class': 'form-control', 'choices': mode_choice})
        }