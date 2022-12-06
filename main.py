#Python Project 4
import copy
from sudoku_generator import SudokuGenerator
#from sudoku_generator import generate_sudoku

# Method to display the user's choice menu
def user_menu():
  print()
  print("1. Sketch Cell")
  print("2. Draw In Board")
  print("3. Reset Board")
  print("4. Exit")
  print()

# Method to display the users playing board
def display_user_board():
  print()
  print('\n'.join([''.join(['{:^4}'.format(item) for item in row]) 
      for row in board]))
  
# Method to display the sudoku solution board
def display_solved_board():
  print()
  print('\n'.join([''.join(['{:^4}'.format(item) for item in row]) 
      for row in solved_board]))

# Prompt the user to initialize the game difficulty
print("Welcome to Sudoku!")
print("1. Easy")
print("2. Medium")
print("3. Hard")
choice = int(input("Select Game Mode: "))
if choice == 1:
    difficulty = 30
elif choice == 2:
    difficulty = 40
elif choice == 3:
    difficulty = 50
else:
    print("Invalid selection!")
    restart = True

# Generate the Sudoku board to be solved this game with size from user difficulty choice
sudoku_obj = SudokuGenerator(9, difficulty)
sudoku_obj.fill_values()
# Create a copy of the solved Sudoku board for this game that can be used for testing win condition
solved_board = copy.deepcopy(sudoku_obj.get_board())
display_solved_board()


# This call for the board is unnecessary now. Just commenting before testing to make sure before I delete it.
#board = sudoku_obj.get_board()


# Generate a copy of the Sudoku board with random cells removed for the user to solve
sudoku_obj.remove_cells()

# Create a copy of the board that will be updated based on the user inputs
board = copy.deepcopy(sudoku_obj.get_board())

# Preserve a copy of the unmodified board for tracking valid cells for user update which are cells that started with 0s
unmodified_board = copy.deepcopy(sudoku_obj.get_board())

# Initializing the game-loop with loop variable game_over
game_over = False
while game_over == False:
  # Printing the update board based on user previous inputs
  display_user_board()
  
  user_menu()
  answer = int(input('Enter your choice: '))

  # Attempt to 'sketch' in the user value
  if answer == 1:
    row = int(input('Enter the row of the cell you would like to modify: '))
    col = int(input('Enter the column of the cell you would like to modify: '))
    if unmodified_board[row][col] != 0:
      print("Invalid cell!")
    else:
      try:
        bad_value = -1
        while bad_value == -1:
          new_cell = str(input('Enter the number you would like to use in this cell: '))
          if int(new_cell) <= 9 and int(new_cell) > 0:
            # Stop the while loop condition enforcing valid user input
            bad_value = 0
          else:
              print("Error. Enter a single digit value 1-9")
      # Creating an exception for catching a character string for user input
          board[row][col] = "'" + new_cell + "'"
      except ValueError:
        new_cell == str(0)
        print("Error. Enter a single digit value 1-9")

  # Draw the user's 'sketched' values in to the sudoku and check for a win or lose
  if answer == 2:
    # Draw each item in the board to a string for stripping the sketch indicator marks off the values of each cell
    for row in board:
      for cell in row:
        cell = str(cell)
        if len(cell) > 1:
          # Stripping the sketch indicators off of each user input cell by taking just the middle (number) value of the cell string
          cell = cell[1]
    if board == solved_board:
      print('You win!')
      game_over = True
    else:
      print('You lose.')
      game_over = True

  if answer == 3:
    print("Resetting the sudoku...")
    board = unmodified_board
    
  if answer == 4:
    print("Thanks for playing! Bye!")
    game_over = True

  # Hidden choice for setting the board to the solved board for troubleshooting the win condition without having to solve the puzzle
  if answer == 9:
    board = solved_board
    

 


