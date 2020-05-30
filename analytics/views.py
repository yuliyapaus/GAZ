from django.shortcuts import render


def analytics(request):
    response = {}
    return render(request, './analytics/analytics.html', response)


def implementation_plan(request):
    response = {}
    return render(request, './analytics/implementation_plan.html', response)


def deviation_analysis(request):
    response = {}
    return render(request, './analytics/deviation_analysis.html', response)


def report_RKDZ(request):
    response = {}
    return render(request, './analytics/report_RKDZ.html', response)
