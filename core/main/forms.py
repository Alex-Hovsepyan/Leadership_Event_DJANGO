from django import forms
from .models import ContactPost

class ContactModelForm(forms.ModelForm):

    class Meta:

        model = ContactPost
        fields = ['user_name', 'user_email', 'subject', 'message']