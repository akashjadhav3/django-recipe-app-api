from django.test import TestCase
from app.calc import add

class CalcTest(TestCase):
    def test_add_two_number(self):
        """ Test that two number are add together"""
        self.assertEqual(add(8,3),11)