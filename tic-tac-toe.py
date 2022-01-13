def main():
  grid_size = 3
  draw_game_board(grid_size)
  
  
  
def draw_game_board(lengthwidth):
  number = 0
  for range(lengthwidth):
    print("| ")
    for range(lengthwidth):
      number += 1
      print(f"{number} |")
  
  
if __name__ == "__main__":
  main()
