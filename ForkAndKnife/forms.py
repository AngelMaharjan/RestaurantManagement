from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,)
    last_name = forms.CharField(max_length=30, required=True, )
    contact_number = forms.CharField(label='Contact Number', max_length=10, required=True)
    address = forms.CharField(label='Address', max_length=255, required=True)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove the password validation error messages
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields+('first_name', 'last_name', 'email', 'address', 'contact_number')
      #  fields = ('first_name', 'last_name','username', 'contact_number','address','email', 'password1', 'password2', )
       # help_texts = {}
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.contact_number = self.cleaned_data.get('contact_number')
        user.address = self.cleaned_data.get('address')
        user.is_staff = self.cleaned_data.get('is_staff', False)
        if commit:
            user.save()
        return user