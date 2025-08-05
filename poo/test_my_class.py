from unittest import TestCase
from my_class import Person

class TestPerson(TestCase):
    
    def test_class_person(self):
        # Arrange
        first_name : str = "Davi"
        last_name : str  = "Nunes"
        age : int =  20
        
        # Act
        person = Person(first_name,last_name,age)

        # Assert
        self.assertEqual(person.first_name,first_name)
        self.assertEqual(person.last_name,last_name)
        self.assertEqual(person.age,age)

