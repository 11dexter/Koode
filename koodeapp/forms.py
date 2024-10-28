from django import forms
from .models import CustomerModel, CallPackageModel, adminmodel
from django.core.exceptions import ValidationError

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = ['customer_first_name', 'customer_last_name', 'customer_email', 'customer_phone_number','customer_password','gender','status']

        labels = {
            'customer_first_name': 'First Name',
            'customer_last_name': 'Last Name',
            'customer_email': 'Email',
            'customer_phone_number': 'Phone Number',
            'customer_password': 'Password',
            'gender': 'Gender',
            'status': 'Status',
        }

        widgets = {
            'customer_first_name': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'First Name'}),
            'customer_last_name': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Last Name'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Email'}),
            'customer_phone_number': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Phone Number'}),
            'customer_password': forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Password'}),
            'gender': forms.Select(choices=CustomerModel.GENDER_CHOICES, attrs={'class': 'form-control form-select', 'placeholder': 'Gender'}),
            'status': forms.Select(choices=CustomerModel.USER_STATUS_CHOICES, attrs={'class': 'form-control form-select', 'placeholder': 'Status'}),

        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('customer_phone_number')
        # Check if the phone number is exactly 10 digits
        if len(phone_number) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits.")

        # Check for uniqueness and provide a custom error message
        if CustomerModel.objects.filter(customer_phone_number=phone_number).exists():
            self.add_error('customer_phone_number','This number already exists.')  # Custom error message

        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("customer_password")

        # Password length check (as an example)
        if password and len(password) < 8:
            self.add_error('customer_password', 'Password must be at least 8 characters long.')



class CallPackageForm(forms.ModelForm):
    class Meta:
        model = CallPackageModel
        fields = ['package_price', 'total_coins']
        widgets = {
            'package_price': forms.NumberInput(
                attrs={'class': 'form-control form-control-user', 'placeholder': 'Enter price'}),
            'total_coins': forms.NumberInput(
                attrs={'class': 'form-control form-control-user', 'placeholder': 'Enter coins'}),
        }


# class AdminForm(forms.ModelForm):
#     class Meta:
#         model = adminmodel
#         fields = ['admin_first_name', 'admin_last_name', 'admin_email', 'admin_password']
#         widgets = {
#             'admin_first_name': forms.TextInput(
#                 attrs={'class': 'form-control form-control-user', 'placeholder': 'First Name'}),
#             'admin_last_name': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Last Name'}),
#             'admin_email': forms.EmailInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Email Address'}),
#             'admin_password': forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Password'}),
#         }

    # repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Repeat Password'}))
    #
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = self.cleaned_data.get("admin_password")
    #     repeat_password = self.cleaned_data.get("repeat_password")
    #
    #     if password != repeat_password:
    #         raise forms.ValidationError("Passwords do not match")
    #
    #     return cleaned_data
