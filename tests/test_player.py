import unittest
from unittest.mock import patch
from source.player import player_pon
class TestPlayerPon(unittest.TestCase):
    @patch('builtins.input', side_effect = '1')
    def test_input_1_returns_goo(self, mock_input):
        result = player_pon()
        self.assertEqual(result, 'グー')
    @patch('builtins.input', side_effect = '2')
    def test_input_2_returns_choki(self, mock_input):
        result = player_pon()
        self.assertEqual(result, 'チョキ')
    @patch('builtins.input', side_effect = '3')
    def test_input_3_returns_paa(self, mock_input):
        result = player_pon()
        self.assertEqual(result, 'パー')
    @patch('builtins.input', side_effect = ['0', '4', '1'])
    def test_invalid_input_then_valid_input(self, mock_input):
        result = player_pon()
        self.assertEqual(result, 'グー')