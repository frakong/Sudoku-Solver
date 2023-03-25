sudoku_puzzle = [
  [1, 0, 1, 0, 1, 0, 1, 0, 1],
  [0, 2, 0, 2, 0, 2, 0, 2, 0],
  [3, 0, 3, 0, 3, 0, 3, 0, 3],
  [0, 4, 0, 4, 0, 4, 0, 4, 0],
  [5, 0, 5, 0, 5, 0, 5, 0, 5],
  [0, 6, 0, 6, 0, 6, 0, 6, 0],
  [7, 0, 7, 0, 7, 0, 7, 0, 7],
  [0, 8, 0, 8, 0, 8, 0, 8, 0],
  [9, 0, 9, 0, 9, 0, 9, 0, 9]
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

print_sudoku_puzzle(sudoku_puzzle)
print(find_first_empty_space(sudoku_puzzle))