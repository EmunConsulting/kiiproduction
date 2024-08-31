# forms.py

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User

from .models import Profile, Post, Comment


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'gender', 'birthdate', 'profile_picture', 'bio', 'country_origin', 'learned_at', 'works_at', 'lives_in', 'address', 'phone_number', 'cover_photo', 'interest', 'website']

        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={
                'placeholder': 'Your bio in brief ...',
                'rows': 3,
            }),
            'interest': forms.Textarea(attrs={
                'placeholder': 'Your interests in brief ...',
                'rows': 3,
            }),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProfileForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['user'].initial = user
            self.fields['user'].disabled = True

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.form_class = 'form-horizontal'  # Optional: adjust form class as needed

    def save(self, commit=True):
        profile = super(ProfileForm, self).save(commit=False)
        if self.fields['user'].initial:
            profile.user = self.fields['user'].initial
        if commit:
            profile.save()
        return profile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'content', 'image', 'video']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'What do you want to share today?',
                'rows': 3,
            }),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['user'].initial = user
            self.fields['user'].disabled = True

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.form_class = 'form-horizontal'

    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        if self.fields['user'].initial:
            post.user = self.fields['user'].initial
        if commit:
            post.save()
        return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'user', 'content',]
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'You can write your comments here.',
                'rows': 3,
            }),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CommentForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['user'].initial = user
            self.fields['user'].disabled = True

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.form_class = 'form-horizontal'

    def save(self, commit=True):
        post = super(CommentForm, self).save(commit=False)
        if self.fields['user'].initial:
            post.user = self.fields['user'].initial
        if commit:
            post.save()
        return post