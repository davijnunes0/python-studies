from unittest import TestCase
from app import conversion

class TestConversion(TestCase):
    def test_should_return_zero_receiveng_32(self):
        self.assertEqual(conversion(32),0)

    def test_should_return_37_77_receveing_100(self):
        self.assertAlmostEqual(conversion(100),37.77,places=1)
    
    def test_should_return__17_77_receveing_0(self):
        self.assertAlmostEqual(
                conversion(0),
                -17.77,
                places=1
                )
