# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from program.models import ProgramPlanner
from application.models import Application
from .models import ServicesProductsList, RegistrationStatusList, DevelopmentStageList, IndustrySectorList, BusinessRecord, OutcomeRecord


class ServicesProductsListForm(forms.ModelForm):
    class Meta:
        model = ServicesProductsList
        fields = ['service_products',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))


class RegistrationStatusListForm(forms.ModelForm):
    class Meta:
        model = RegistrationStatusList
        fields = ['registration_status',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))


class DevelopmentStageListForm(forms.ModelForm):
    class Meta:
        model = DevelopmentStageList
        fields = ['development_stage',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))


class IndustrySectorListForm(forms.ModelForm):
    class Meta:
        model = IndustrySectorList
        fields = ['industry_sector',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))


class BusinessRecordForm(forms.ModelForm):
    class Meta:
        model = BusinessRecord
        fields = ['user', 'business_model', 'name', 'location', 'services_products', 'registration_status', 'development_stage', 'industry_sector', 'progress_metrics', 'start_date',]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(BusinessRecordForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['user'].initial = user
            self.fields['user'].disabled = True

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.form_class = 'form-horizontal'

    def save(self, commit=True):
        post = super(BusinessRecordForm, self).save(commit=False)
        if self.fields['user'].initial:
            post.user = self.fields['user'].initial
        if commit:
            post.save()
        return post


class OutcomeRecordForm(forms.ModelForm):
    class Meta:
        model = OutcomeRecord
        fields = ['business_record', 'milestone_achieved', 'revenue', 'exit_strategy',]

    def __init__(self, *args, **kwargs):
        business_record = kwargs.pop('business_record', None)
        super(OutcomeRecordForm, self).__init__(*args, **kwargs)

        if business_record:
            self.fields['business_record'].initial = business_record
            self.fields['business_record'].disabled = True

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.form_class = 'form-horizontal'

    def save(self, commit=True):
        post = super(OutcomeRecordForm, self).save(commit=False)
        if self.fields['business_record'].initial:
            post.business_record = self.fields['business_record'].initial
        if commit:
            post.save()
        return post

