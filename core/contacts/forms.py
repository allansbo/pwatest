from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from core.contacts.models import Contact


class ContactForm(forms.ModelForm):

    phone = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='BR'))

    class Meta:
        model = Contact
        fields = '__all__'
