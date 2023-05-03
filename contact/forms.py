from django import forms
from .models import Contact
from django.core.validators import validate_email

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'society', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'autofocus': True}),
            # 'email': forms.EmailInput(),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)
        except:
            raise forms.ValidationError('Invalid email address')
        return email