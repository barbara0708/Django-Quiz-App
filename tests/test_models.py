from django.test import TestCase
from category.models import Quiz

class QuizClassTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Quiz.objects.create(quiz_name='Quiz Name',desc='Description to the quiz')
    
    def check_quiz_name_label(self):
        quiz=Quiz.objects.get(id=1)
        label=quiz._meta.get_field('quiz_name').verbose_name
        self.assertEqual(label,'quiz name')
    
