from planes import views
from django.urls import path

app_name = "planes"

urlpatterns = [
    path('', views.plane, name='plane' ),
    path('<int:finance_cost_id>/curators/', views.curators, name='curators'),
    path('to_server/', views.from_js, name='from_js'),
    path('<int:item_id>/edit-plane', views.edit_plane, name='edit_plane'),
    path('<int:finance_cost_id>/add/', views.add, name= 'add')
]
