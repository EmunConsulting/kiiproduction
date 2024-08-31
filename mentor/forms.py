# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from program.models import ProgramPlanner
from application.models import Application
from .models import MentorList, Mentorship, MentorComRec


class MentorListForm(forms.ModelForm):
    class Meta:
        model = MentorList
        fields = ['user', 'expertise', 'assigned_on', 'assigned_until',]
        widgets = {
            'assigned_on': forms.DateInput(attrs={'type': 'date'}),
            'assigned_until': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))


class MentorshipForm(forms.ModelForm):
    class Meta:
        model = Mentorship
        fields = ['user', 'program', 'mentor', 'assigned_on', 'assigned_until']
        widgets = {
            'assigned_on': forms.DateInput(attrs={'type': 'date'}),
            'assigned_until': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))


class MentorComRecForm(forms.ModelForm):
    class Meta:
        model = MentorComRec
        fields = ['mentorship', 'comment', 'recommendation',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))
