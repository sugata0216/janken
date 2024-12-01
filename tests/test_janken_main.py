import unittest
from unittest.mock import patch
from source.janken_main import play_round, display_final, main
class TestJankenMain(unittest.TestCase):
    @patch('builtins.input', side_effect = '1')
    @patch('random.choice')
    @patch('janken_main.play_round')
    def test_game_draw(self, mock_player_pon, mock_computer_pon, mock_judge):
        mock_computer_pon.return_value = 'グー'
        victory_or_defeat = play_round(1)
        self.assertEqual(victory_or_defeat, None)
    @patch('builtins.input', side_effect = '2')
    @patch('random.choice')
    @patch('janken_main.play_round')
    def test_game_win(self, mock_player_pon, mock_computer_pon, mock_judge):
        mock_computer_pon.return_value = 'パー'
        victory_or_defeat = play_round(1)
        self.assertEqual(victory_or_defeat, 'player_win')
    @patch('builtins.input', side_effect = '3')
    @patch('random.choice')
    @patch('janken_main.play_round')
    def test_game_lose(self, mock_player_pon, mock_computer_pon, mock_judge):
        mock_computer_pon.return_value = 'チョキ'
        victory_or_defeat = play_round(1)
        self.assertEqual(victory_or_defeat, 'computer_win')
    def test_display_final_win(self):
        result = display_final(2, 1)
        self.assertEqual(result, 'あなたの総合勝利です!')
    def test_display_final_lose(self):
        result = display_final(1, 2)
        self.assertEqual(result, 'コンピューターの総合勝利です!')