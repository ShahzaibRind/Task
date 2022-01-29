from dataclasses import fields
from operator import mod
from django import forms
from .models import AddEvent


class BookEventForm(forms.ModelForm):
    class Meta:
        model = AddEvent
        fields = ["title", "date_posted", "detail"]