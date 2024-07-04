from django.db import models

class Candidate(models.Model):
    full_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    skills = models.TextField()
    work_format = models.CharField(max_length=255)

class Vacancy(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    skills = models.TextField()
    work_format = models.CharField(max_length=255)
    num_candidates = models.IntegerField()
