from django.urls import path
from django.views.generic import TemplateView

from telemob.main.views import index, politician_list, report_contact


urlpatterns = [
    path('', index, name='index'),
    path('politicos/<int:campaign_id>/', politician_list, name='state_list'),
    path('politicos/<int:campaign_id>/<str:uf>/', politician_list, name='politician_list'),
    path('contato/<int:campaign_id>/<int:politician_id>/', report_contact, name='report_contact'),
    path('sobre/', TemplateView.as_view(template_name="about.html"), name='about'),
]
