from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompanyListView.as_view(), name='company-list'),
    path('companies/<int:id>/', views.CompanyDetailView.as_view(), name='company-detail'),
    path('companies/<int:id>/vacancies/', views.VacancyByCompanyView.as_view(), name='vacancies-by-company'),
    path('vacancies/', views.VacancyListView.as_view(), name='vacancy-list'),
    path('vacancies/<int:id>/', views.VacancyDetailView.as_view(), name='vacancy-detail'),
    path('vacancies/top_ten/', views.TopTenVacanciesView.as_view(), name='top-ten-vacancies'),
]
