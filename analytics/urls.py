from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import get_analytics_page, get_implementation_plan_page

app_name = "analytics"


urlpatterns = [
    path('', get_analytics_page, name='analytics'),
    # path('implementation_plan_page/', get_implementation_plan_page),
    # path('Deviation_analysis/', get_deviation_analysis),
    # path('Report_RKDZ/', get_report_RKDZ),

]
