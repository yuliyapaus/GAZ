from django.shortcuts import render


def get_analytics_page(request):
    response = {"name": 1, 'email': 2}
    return render(request, './analytics/analytics.html', response)


def get_implementation_plan_page(request):
    response = {"name": 1, 'email': 2}
    return render(request, './analytics/implementation_plan.html', response)
