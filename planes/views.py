from django.shortcuts import render, redirect
from .models import PlanningYearFunding
from .forms import SelectPlanForm, PlanningYearFundingForm
from django.forms import modelformset_factory

# Create your views here.

def index(request):
    PlanningYearFundingFormset = modelformset_factory(PlanningYearFunding, form=PlanningYearFundingForm, can_delete=True)

    print(request.POST.get('test1'))
    # print(request.POST)
    form = SelectPlanForm(request.POST or None)
    formset = PlanningYearFundingFormset(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            year = form.cleaned_data['year']
            funding = form.cleaned_data['funding']
            # print(year, funding)

            if formset.is_valid():
                formset.save()

            formset = PlanningYearFundingFormset(queryset=PlanningYearFunding.objects
                                                 .filter(year=year, funding=funding)
                                                 .order_by('year__title', 'funding__title')
                                                 )

    context = {
        'formset': formset,
        'select_form': form
    }
    return render(request, 'index.html', context)