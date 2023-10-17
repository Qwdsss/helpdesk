from django import forms
from .models import Problem


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['phone', 'email', 'description', 'priority']


class ProblemDetailForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['actions', 'status']