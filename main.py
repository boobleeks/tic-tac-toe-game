import random

def tic_tac_toe(a):
      is_over = False
      while not is_over:
            print(f"______________\n|[{a[0]}] [{a[1]}] [{a[2]}]|\n|[{a[3]}] [{a[4]}] [{a[5]}]|\n|[{a[6]}] [{a[7]}] [{a[8]}]|\n______________")
            not_okay = True
            while not_okay:
                  equos = int(input("Choose the cell for X: "))
                  if a[equos-1] == "X" or a[equos-1] == "O":
                        print("Cell is not empty, choose another")
                        print(a[equos-1])
                  else:
                        a[equos-1] = 'X'
                        not_okay = False
            print(f"______________\n|[{a[0]}] [{a[1]}] [{a[2]}]|\n|[{a[3]}] [{a[4]}] [{a[5]}]|\n|[{a[6]}] [{a[7]}] [{a[8]}]|\n______________")
            if (
                    (a[0] == 'X' and a[1] == 'X' and a[2] == 'X') or
                    (a[3] == 'X' and a[4] == 'X' and a[5] == 'X') or
                    (a[6] == 'X' and a[7] == 'X' and a[8] == 'X') or
                    (a[0] == 'X' and a[3] == 'X' and a[6] == 'X') or
                    (a[1] == 'X' and a[4] == 'X' and a[7] == 'X') or
                    (a[2] == 'X' and a[5] == 'X' and a[8] == 'X') or
                    (a[0] == 'X' and a[4] == 'X' and a[8] == 'X') or
                    (a[2] == 'X' and a[4] == 'X' and a[6] == 'X')
            ):
                  print(' X - Won The Game')
                  is_over = True
                  break
            elif a.count('X') >= 5:
                  print('DRAW')
                  break
            not_okay = True
            while not_okay:
                  circle = int(input("Choose the cell for O: "))
                  if a[circle - 1] == "X" or a[circle - 1] == "O":
                        print("Cell is not empty, choose another")
                  else:
                        a[circle-1] = 'O'
                        not_okay = False
            if (
                    (a[0] == 'O' and a[1] == 'O' and a[2] == 'O') or
                    (a[3] == 'O' and a[4] == 'O' and a[5] == 'O') or
                    (a[6] == 'O' and a[7] == 'O' and a[8] == 'O') or
                    (a[0] == 'O' and a[3] == 'O' and a[6] == 'O') or
                    (a[1] == 'O' and a[4] == 'O' and a[7] == 'O') or
                    (a[2] == 'O' and a[5] == 'O' and a[8] == 'O') or
                    (a[0] == 'O' and a[4] == 'O' and a[8] == 'O') or
                    (a[2] == 'O' and a[4] == 'O' and a[6] == 'O')
            ):
                  print(' O - Won The Game')
                  is_over = True


def ai_play(a, computer_set):
      is_over = False
      while not is_over:
            print(f"______________\n|[{a[0]}] [{a[1]}] [{a[2]}]|\n|[{a[3]}] [{a[4]}] [{a[5]}]|\n|[{a[6]}] [{a[7]}] [{a[8]}]|\n______________")
            not_okay = True
            while not_okay:
                  equos = int(input("Choose the cell for X: "))
                  if a[equos - 1] == "X" or a[equos - 1] == "O":
                        print("Cell is not empty, choose another")
                        print(a[equos - 1])
                  else:
                        a[equos - 1] = 'X'
                        computer_set.remove(equos)
                        not_okay = False
            print(f"______________\n|[{a[0]}] [{a[1]}] [{a[2]}]|\n|[{a[3]}] [{a[4]}] [{a[5]}]|\n|[{a[6]}] [{a[7]}] [{a[8]}]|\n______________")
            if (
                    (a[0] == 'X' and a[1] == 'X' and a[2] == 'X') or
                    (a[3] == 'X' and a[4] == 'X' and a[5] == 'X') or
                    (a[6] == 'X' and a[7] == 'X' and a[8] == 'X') or
                    (a[0] == 'X' and a[3] == 'X' and a[6] == 'X') or
                    (a[1] == 'X' and a[4] == 'X' and a[7] == 'X') or
                    (a[2] == 'X' and a[5] == 'X' and a[8] == 'X') or
                    (a[0] == 'X' and a[4] == 'X' and a[8] == 'X') or
                    (a[2] == 'X' and a[4] == 'X' and a[6] == 'X')
            ):
                  print(' X - Won The Game')
                  is_over = True
                  break
            elif a.count('X') >= 5:
                  print('DRAW')
                  break

            circle = random.choice(computer_set)
            a[circle - 1] = 'O'
            computer_set.remove(circle)
            print(f'computer chose: {circle} cell')
            if (
                    (a[0] == 'O' and a[1] == 'O' and a[2] == 'O') or
                    (a[3] == 'O' and a[4] == 'O' and a[5] == 'O') or
                    (a[6] == 'O' and a[7] == 'O' and a[8] == 'O') or
                    (a[0] == 'O' and a[3] == 'O' and a[6] == 'O') or
                    (a[1] == 'O' and a[4] == 'O' and a[7] == 'O') or
                    (a[2] == 'O' and a[5] == 'O' and a[8] == 'O') or
                    (a[0] == 'O' and a[4] == 'O' and a[8] == 'O') or
                    (a[2] == 'O' and a[4] == 'O' and a[6] == 'O')
            ):
                  print(' O - Won The Game')
                  is_over = True


a = [
      1,2,3,
      4,5,6,
      7,8,9
]
computer_set = [
      1,2,3,
      4,5,6,
      7,8,9
]

is_game_over = False
while not is_game_over:
      print('WELCOME TO TIC TAC TOE GAME')
      game_mode = input('Type "A" to play with friend\nType "B" to play with computer\nType: ')
      if game_mode == "A":
            tic_tac_toe(a)
      elif game_mode == "B":
            ai_play(a, computer_set)
      ask_to_continue = input("Do u want ot play again? (Type 'Y' or 'N'): ")
      if ask_to_continue == 'Y':
            continue
      else:
            break
