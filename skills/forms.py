from django import forms

from .models import JobRecord


class JobForm(forms.ModelForm):

    class Meta:
        model = JobRecord

        fields = ('title', 'city', 'state', 'low_salary', 'high_salary', 'typical_day', 'avg_day',
        'tech_used', 'requirements', 'skills', 'benefit',)


