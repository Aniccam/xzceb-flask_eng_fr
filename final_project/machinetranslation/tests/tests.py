import unittest
from translator import english_to_french, french_to_english
"""
This class test the correction of the translation mathods
"""
class TestTranslator(unittest.TestCase):
    def test_fr2en(self):
        """
        This method has test for french to english
        """
        self.assertNotEqual(french_to_english(" "), "Hello") # test when null is given as input the output is null 
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test when "Bonjour" is given as input the output is "Hello" 
        

    def test_en2fr(self):
        """
        This method has two tests for english to french 
        """
        self.assertNotEqual(english_to_french(" "), "Bonjour") # test when null is given as input the output is null 
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test when "Hello" is given as input the output is "Bonjour" 

     

unittest.main()