from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    Form for submitting collaboration requests.
    This form is used to collect the name, email, and message from users
    who wish to collaborate.
    It includes fields for the user's name, email address, and a message.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')