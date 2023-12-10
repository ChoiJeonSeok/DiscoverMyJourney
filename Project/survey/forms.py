from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['gender', 'age', 'family','region_1', 'area_1','region_2', 'area_2','region_3', 'area_3']