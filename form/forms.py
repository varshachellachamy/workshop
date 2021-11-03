from django import forms
from .models import RegForm


class Form(forms.ModelForm):
    class Meta:
        model = RegForm
        fields = "__all__"