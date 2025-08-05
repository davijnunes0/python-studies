from conversion_temp import conversion_to_farenheit_to_celsius
from conversion_temp import conversion_to_celsius_to_farenheit
from unittest import TestCase

class TestConversionFarenheitToCelsius(TestCase):
    def test_converte_deve_retornar_0_quando_receber_32(self):
         self.assertEqual(conversion_to_farenheit_to_celsius(32),0)

    def test_deve_retornar_40_quando_receber_40(self):
        self.assertEqual(conversion_to_farenheit_to_celsius(-40),-40)

    def test_deve_retornar_17_77_quando_receber_0(self):
         self.assertAlmostEqual(conversion_to_farenheit_to_celsius(0),-17.77,places=1)


    def test_multiples_value(self):       
        values : list[int] = [(212,100), (98.7,37.0555)]
        for input_,output in values:
            with self.subTest(input_=input_,output=output):
                self.assertAlmostEqual(
                        conversion_to_farenheit_to_celsius(input_),
                        output,places=2
        )

class TestConversionCelsiustoFarenheit(TestCase): 
    def test_deve_retornar_89_6_quando_receber_32(self):
        self.assertAlmostEqual(conversion_to_celsius_to_farenheit(32),89.6,places=1)

