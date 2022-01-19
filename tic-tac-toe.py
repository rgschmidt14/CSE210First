'''This is the Tic Tac Toe Game by R. Gunnar Schmidt in CSE 210 - Section 20 - BYU Idaho - Brother Duane Richards'''



def main():
  default_grid_size = 3
  grid_size = default_grid_size #may add coding later to allow for user inputted size
  turn = True
  xvariables = []
  yvariables = []
  play_again = True
  reset_board = False


  def draw_game_board(xmarks=xvariables,ymarks=yvariables,lengthwidth=3):
    number = 0
    for i in range(lengthwidth):
      printline = []
      for j in range(lengthwidth):
        number += 1
        if number in xmarks:
          printline.append("X")
        elif number in ymarks:
          printline.append("Y")
        else:
          printline.append(number)
      print(printline)

  def check_for_winner(v):
    win = False
    if 1 in v and 2 in v and 3 in v:
      win = True
    elif 4 in v and 5 in v and 6 in v:
      win = True
    elif 7 in v and 8 in v and 9 in v:
      win = True
    elif 1 in v and 4 in v and 7 in v:
      win = True
    elif 2 in v and 5 in v and 8 in v:
      win = True
    elif 3 in v and 6 in v and 9 in v:
      win = True
    elif 1 in v and 5 in v and 9 in v:
      win = True
    elif 3 in v and 5 in v and 7 in v:
      win = True
    return win


  while play_again == True:
    if reset_board == True:
      xvariables = []
      yvariables = []
    reset_board = False


    if turn == True:  #True is an X's turn, while False is a Y's turn
      try_again = True
      while try_again:
        draw_game_board(lengthwidth=grid_size)
        xturn = int(input("It is now X's turn, go ahead and place an X by inputting the corresponding number: "))
        if xturn not in xvariables and xturn not in yvariables:
          xvariables.append(xturn)
          try_again = False
        else:
          print("That number is taken, try again.")

      
    else:
      try_again = True
      while try_again == True:
        draw_game_board(lengthwidth=grid_size)
        yturn = int(input("It is now Y's turn, go ahead and place a Y by inputting the corresponding number: "))
        if yturn not in xvariables and yturn not in yvariables:
          yvariables.append(yturn)
          try_again = False
        else:
          print("That number is taken, try again.")

    if check_for_winner(xvariables):
      draw_game_board(lengthwidth=grid_size)
      print("Congratulations! X has won!")
      '''
      play_again_question = input("Congratulations! X has won! Ready for another round? Y/N ").upper()
      if play_again_question == "Y":
        play_again = True
        reset_board = True
      else:
      '''
      play_again = False
      print("Thanks for playing! Have a good rest of your day! :)")
    elif check_for_winner(yvariables):
      draw_game_board(lengthwidth=grid_size)
      print("Congrats Y! You've won!")
      '''
      play_again_question = input("Congrats Y! You've won! Do you want to play another game? Y/N ").upper()
      if play_again_question == "Y":
        play_again = True
        reset_board = True
      else:
      '''
      play_again = False
      print("Thanks for playing! Have a good rest of your day! :)")
    turn = toggle_true_false(turn)


  

    

  
  
def toggle_true_false(x):
  y = False
  if x == False:
    y = True
  return y
  
  
if __name__ == "__main__":
  main()
