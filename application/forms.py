# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from program.models import ProgramPlanner
from application.models import Application
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['user', 'program']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        program_id = kwargs.pop('pk', None)
        super(ApplicationForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['user'].initial = user
            self.fields['user'].disabled = True

        if program_id:
            program = ProgramPlanner.objects.get(pk=program_id)  # Use ProgramPlanner here
            self.fields['program'].initial = program
            self.fields['program'].disabled = True

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.form_class = 'form-horizontal'

    def save(self, commit=True):
        post = super(ApplicationForm, self).save(commit=False)
        if self.fields['user'].initial:
            post.user = self.fields['user'].initial
        if self.fields['program'].initial:
            post.program = self.fields['program'].initial
        if commit:
            post.save()
        return post
