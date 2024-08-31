# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from program.models import ProgramPlanner
from application.models import Application
from .models import FundTypeList, FundRecord, InvestorTypeList, InvestorRecord, InvestmentRecord


class FundTypeListForm(forms.ModelForm):
    class Meta:
        model = FundTypeList
        fields = ['fund_type',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))


class FundRecordForm(forms.ModelForm):
    class Meta:
        model = FundRecord
        fields = ['user', 'fund_type', 'amount', 'funded_by', 'terms', 'date_provided',]
        widgets = {
            'date_provided': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(FundRecordForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['user'].initial = user
            self.fields['user'].disabled = True

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.form_class = 'form-horizontal'

    def save(self, commit=True):
        post = super(FundRecordForm, self).save(commit=False)
        if self.fields['user'].initial:
            post.user = self.fields['user'].initial
        if commit:
            post.save()
        return post


class InvestorTypeListForm(forms.ModelForm):
    class Meta:
        model = InvestorTypeList
        fields = ['investor_type',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))


class InvestorRecordForm(forms.ModelForm):
    class Meta:
        model = InvestorRecord
        fields = ['investor', 'investor_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))