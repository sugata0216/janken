import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))
import player
import computer
import janken_judge
def play_round(round):
    print(f"-----ラウンド {round} -----")
    computer_hand = computer.computer_pon()
    player_hand = player.player_pon()
    result = janken_judge.judge(computer_hand, player_hand)
    print(f'あなたの手:{player_hand}')
    print(f'コンピューターの手:{computer_hand}')
    print('')
    if result == 'draw':
      print('あいこです!再度対決!')
      return None
    elif result == 'player_win':
      print('あなたの勝ちです!')
      return 'player_win'
    else:
      print('コンピューターの勝ちです!')
      return 'computer_win'
def display_final(player, computer):
    print(f'【最終結果】')
    print(f'あなた:{player}勝')
    print(f'コンピューター:{computer}勝')
    if player > computer:
      return 'あなたの総合勝利です!'
    else:
      return 'コンピューターの総合勝利です!'
def main():
   player_win = 0
   computer_win = 0

   """3回戦のじゃんけんゲームを行う関数"""
   # hands = ['グー', 'チョキ', 'パー']

   round = 1
   while round <= 3:
       result = play_round(round)    
       if result == 'player_win':
          player_win +=1
          round += 1
       elif result == 'computer_win':
          computer_win +=1
          round += 1            
       print("")
   final_result = display_final(player_win, computer_win)
   print(final_result)
if __name__ == '__main__':
   main()