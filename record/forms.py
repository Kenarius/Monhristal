from django import forms
from . import models
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ('name', 'body', 'record_type')


class RecordsForm(forms.ModelForm):
    class Meta:
        model = models.Records
        fields = ('name', 'body', 'record_type')
