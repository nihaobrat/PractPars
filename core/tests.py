from django.test import TestCase
from .models import Candidate

class CandidateTestCase(TestCase):
    def setUp(self):
        Candidate.objects.create(full_name="John Doe", job_title="Developer")

    def test_candidate_creation(self):
        candidate = Candidate.objects.get(full_name="John Doe")
        self.assertEqual(candidate.job_title, "Developer")

