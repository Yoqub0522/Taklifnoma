from django.urls import path
from . import views

urlpatterns = [
    path('', views.invitation_page, name='invitation'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('save-response/', views.save_response, name='save_response'),
    path('stats/', views.get_responses_stats, name='get_stats'),
]