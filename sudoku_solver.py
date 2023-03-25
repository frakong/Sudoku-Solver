sudoku_puzzle = [
  [9, 0, 3, 5, 6, 0, 4, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 6, 0],
  [0, 5, 0, 0, 0, 2, 0, 0, 0],
  [4, 0, 0, 0, 0, 0, 0, 0, 7],
  [0, 9, 0, 3, 8, 0, 0, 2, 0],
  [0, 0, 0, 0, 0, 5, 0, 0, 0],
  [0, 0, 8, 0, 0, 0, 2, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0, 0],
  [0, 3, 0, 6, 9, 0, 0, 8, 0]
]

def print_sudoku_puzzle(sudoku_puzzle):
  for row_number, row in enumerate(sudoku_puzzle):
    if row_number != 0 and row_number % 3 == 0:
      print ("- - - - - - - - - - - -")
      # will start a new line so we can print next row without having to increment row_number
    for column_number, value in enumerate(row):
      if column_number != 0 and column_number % 3 == 0:
        print(" | ", end="")
      if column_number != 8 and value != 0:
        print(str(value) + " ", end="")
      elif column_number != 8 and value == 0:
        print(" ", end=" ")
      elif column_number == 8 and value != 0:
        print(str(value))
      else:
        print(" ")

def find_first_empty_space(sudoku_puzzle):
  for row_number, row in enumerate(sudoku_puzzle):
    for column_number, value in enumerate(row):
      if value == 0:
        return (row_number, column_number)
  return -1

def is_valid_in_row(sudoku_puzzle, current_number, current_position):
  for column in range(len(sudoku_puzzle[0])):
    if sudoku_puzzle[current_position[0]][column] == current_number and column != current_position[1]:
      return False
  return True

def is_valid_in_column(sudoku_puzzle, current_number, current_position):
  for row in range(len(sudoku_puzzle)):
    if sudoku_puzzle[row][current_position[1]] == current_number and row != current_position[0]:
      return False
  return True

def is_valid_in_box(sudoku_puzzle, current_number, current_position):
  current_box_row = current_position[0] // 3
  current_box_column = current_position[1] // 3
  for row_in_box in range(current_box_row*3, current_box_row*3+3):
    for column_in_box in range(current_box_column*3, current_box_column*3+3):
      if (sudoku_puzzle[row_in_box][column_in_box] == current_number and (row_in_box, column_in_box) != current_position):
        return False
  return True

def is_puzzle_valid(sudoku_puzzle, current_number, current_position):
  # Current position should be a tuple (row, col)
  if (is_valid_in_row(sudoku_puzzle, current_number, current_position) and is_valid_in_column(sudoku_puzzle, current_number, current_position) and is_valid_in_box(sudoku_puzzle, current_number, current_position)):
    return True
  return False 

def solve_puzzle(sudoku_puzzle):
  # Takes a sudoku puzzle and solves it through backtracking. Assumes that every number already in the puzzle is valid.
  first_empty_space = find_first_empty_space(sudoku_puzzle)
  if (first_empty_space == -1):
    #No empty spaces, so puzzle is solved.
    return True
  else:
    empty_space_row, empty_space_col = first_empty_space
  
  #Now, try plugging each possible number (1-9) into the empty space and see if it's valid.
  for test_number in range(1,10):
    if (is_puzzle_valid(sudoku_puzzle, test_number, (empty_space_row, empty_space_col))):
      #Add the test number to the empty space and try to solve the updated board.
      sudoku_puzzle[empty_space_row][empty_space_col] = test_number;
      if (solve_puzzle(sudoku_puzzle)):
        return True
      #If you can't solve the updated board, the test number is invalid, reset empty space to 0.
      sudoku_puzzle[empty_space_row][empty_space_col] = 0
  return False

def solve_sudoku_puzzle(sudoku_puzzle):
  #Solves the sudoku puzzle and prints the puzzle before and after it is solved.
  print_sudoku_puzzle(sudoku_puzzle)
  solve_puzzle(sudoku_puzzle)
  print_sudoku_puzzle(sudoku_puzzle)

solve_sudoku_puzzle(sudoku_puzzle)