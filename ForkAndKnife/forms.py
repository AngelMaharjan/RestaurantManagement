

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer
from django.core.validators import RegexValidator


#from django.contrib.auth.models import User

# Create a custom form that extends UserCreationForm
class CustomUserCreationForm(UserCreationForm):

    address = forms.CharField(max_length=200)
    #phone_number = forms.CharField(max_length=10)
    numeric_validator = RegexValidator(r'^[0-9]*$', 'Only numeric values are allowed for the phone number.')
    phone_number = forms.CharField(max_length=10, validators=[numeric_validator])

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError('Only numeric values are allowed for the phone number.')
        return phone_number

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the password validation error messages
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None      
        # Remove the username validation error message
        self.fields['username'].help_text = None
    # Use the User model and include the new fields in the form
    class Meta:
        
        model = Customer
        fields = ('username', 'email', 'first_name', 'last_name', 'email', 'address', 'phone_number')

    # Override the save() method to set the first name and last name fields
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = self.cleaned_data.get('is_staff', False)
        
        # Save the user to the database
        if commit:
            user.save()
        return user
