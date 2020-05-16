from django import forms
from django.forms.widgets import Select
from .models import Planning

class PlanningForm(forms.ModelForm):
    delete = forms.BooleanField(label='удалить', required=False)
    class Meta:
        model = Planning
        fields = (
            'FinanceCosts', 'curator', 'year',
            'first_quart', 'second_quart', 'third_quart', 
            'fourth_quart', 'period', 'delete'
            )
        labels={
            'FinanceCost':'Статья финансирования',
            'curator':'Куратор',
            'year':'Год',
            'first_quart':'Квартал 1',
            'second_quart':'Квартал 2',
            'third_quart':'Квартал 3',
            'fourth_quart':'Квартал 4',
            'period':'Период хз'
        }