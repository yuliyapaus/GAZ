from  django.forms import Form, ModelForm, ModelChoiceField
from .models import YearPeriod, FinanceCosts, PlanningYearFunding


class SelectPlanForm(Form):
    year = ModelChoiceField(queryset=YearPeriod.objects.all(), label='Год')
    funding = ModelChoiceField(queryset=FinanceCosts.objects.all(), label='Статья финансирования')


class PlanningYearFundingForm(ModelForm):
    class Meta:
        model = PlanningYearFunding
        fields = '__all__'
        # exclude = ['year', 'funding']
        labels = {
            'funding': 'Статья',
            'sum_q1': '1-й квартал',
            'sum_q2': '2-й квартал',
            'sum_q3': '3-й квартал',
            'sum_q4': '4-й квартал',
        }