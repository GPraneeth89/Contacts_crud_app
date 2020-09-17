from django import forms
from phonebook.models import Contacts

class ContactsForm(forms.ModelForm):
    class Meta:
        model=Contacts
        fields="__all__"
        