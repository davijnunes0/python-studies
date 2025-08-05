from unittest import TestCase
from function import multiple_n,sum_n
class TestFunction(TestCase):
    
    def test_sum_more_five(self):
        sum_more_five = sum_n(5)
        answer_sum_more_five = sum_more_five(10)
        self.assertEqual(sum_more_five(10),answer_sum_more_five)

    def test_multiple_n(self):
        multiple_by_teen = multiple_n(10)
        answer_multiple_by_teen = multiple_by_teen(2)
        self.assertEqual(multiple_by_teen(2),answer_multiple_by_teen)
