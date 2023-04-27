'''from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,)
    last_name = forms.CharField(max_length=30, required=True, )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove the password validation error messages
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields+('first_name', 'last_name', 'email', )
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.is_staff = self.cleaned_data.get('is_staff', False)
        if commit:
            user.save()
        return user '''

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create a custom form that extends UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    
    # Add fields for first name and last name
    first_name = forms.CharField(max_length=30, required=True,)
    last_name = forms.CharField(max_length=30, required=True, )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the password validation error messages
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None      
        # Remove the username validation error message
        self.fields['username'].help_text = None
    # Use the User model and include the new fields in the form
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields+('first_name', 'last_name', 'email', )  
    # Override the save() method to set the first name and last name fields
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.is_staff = self.cleaned_data.get('is_staff', False)
        
        # Save the user to the database
        if commit:
            user.save()
        return user
