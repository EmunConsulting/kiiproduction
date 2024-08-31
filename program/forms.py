# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User

from .models import ProgramCategoryList, ProgramList, ProgramPlanner


class ProgramCategoryListForm(forms.ModelForm):
    class Meta:
        model = ProgramCategoryList
        fields = ['program_category',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))


class ProgramListForm(forms.ModelForm):
    class Meta:
        model = ProgramList
        fields = ['program_name', 'program_category', 'active',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))


class ProgramPlannerForm(forms.ModelForm):
    class Meta:
        model = ProgramPlanner
        fields = ['program_name', 'duration', 'resources_provided', 'start_date', 'end_date',]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))

