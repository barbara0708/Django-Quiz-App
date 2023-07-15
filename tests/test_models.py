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
    
    def check_category_label(self):
        quiz=Quiz.objects.get(id=1)
        label=quiz._meta.get_field('category').verbose_name
        self.assertEqual(label,'category')

    def quiz_name_max_length(self):
        quiz=Quiz.objects.get(id=1)
        max_length=quiz._meta.get_field('quiz_name').max_length
        self.assertEqual(max_length,'100')
