from django.shortcuts import render
from rest_framework import viewsets
from .models import Candidate, Vacancy
from .serializers import CandidateSerializer, VacancySerializer

def index(request):
    return render(request, 'index.html')

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
