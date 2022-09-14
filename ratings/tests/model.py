from django.test import TestCase
from ratings.models import Students



class TestAppModels(TestCase):
    def test_model_str(self):
        student_scores= Students.objects.create(student_scores ="Django.Testing")
        content= Students.objects.create(cotent="this is content")
        self.assertEqual(str(student_scores), "Django Testing" )
        # self.assertEqual(str(content),"this is content")

