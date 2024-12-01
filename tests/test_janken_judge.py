import unittest
from source.janken_judge import judge
class TestJankenJudge(unittest.TestCase):
    def test_judge_draw(self):
        patterns = [('グー', 'グー'), ('チョキ', 'チョキ'), ('パー', 'パー')]
        for computer_hand, player_hand in patterns:
            result = judge(computer_hand, player_hand)
            self.assertEqual(result, 'draw')
    def test_judge_win(self):
        patterns = [('グー', 'パー'), ('チョキ', 'グー'), ('パー', 'チョキ')]
        for computer_hand, player_hand in patterns:
            result = judge(computer_hand, player_hand)
            self.assertEqual(result, 'player_win')
    def test_judge_lose(self):
        patterns = [('グー', 'チョキ'), ('チョキ', 'パー'), ('パー', 'グー')]
        for computer_hand, player_hand in patterns:
            result = judge(computer_hand, player_hand)
            self.assertEqual(result, 'computer_win')