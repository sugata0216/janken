import unittest
from unittest.mock import patch
from source.computer import computer_pon
class TestComputerPon(unittest.TestCase):
    @patch('random.choice')
    def test_computer_pon_goo(self, mock_choice):
        mock_choice.return_value = 'グー'
        result = computer_pon()
        self.assertEqual(result, 'グー')
    @patch('random.choice')
    def test_computer_pon_choki(self, mock_choice):
        mock_choice.return_value = 'チョキ'
        result = computer_pon()
        self.assertEqual(result, 'チョキ')
    @patch('random.choice')
    def test_computer_pon_paa(self, mock_choice):
        mock_choice.return_value = 'パー'
        result = computer_pon()
        self.assertEqual(result, 'パー')