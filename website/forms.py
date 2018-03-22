# -*- coding: utf-8 -*-
from django.forms import ModelForm

from website.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'mail', 'cell_phone', 'message')
