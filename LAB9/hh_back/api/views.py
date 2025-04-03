from rest_framework import generics
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer

#all companies
class CompanyListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

#single company
class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

#all vacancies
class VacancyListView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

#single vacancy
class VacancyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

#top 10 vacancies by salary
class TopTenVacanciesView(generics.ListAPIView):
    queryset = Vacancy.objects.all().order_by('-salary')[:10]
    serializer_class = VacancySerializer

#vacancies by company
class VacancyByCompanyView(generics.ListAPIView):
    serializer_class = VacancySerializer

    def get_queryset(self):
        company_id = self.kwargs['id']
        return Vacancy.objects.filter(company_id=company_id)
