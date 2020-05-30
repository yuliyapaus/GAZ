from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import analytics, implementation_plan, deviation_analysis, report_RKDZ

app_name = "analytics"


urlpatterns = [
    path('', analytics, name='analytics'),
    path('implementation_plan/', implementation_plan),
    path('deviation_analysis/', deviation_analysis),
    path('report_RKDZ/', report_RKDZ),

]
