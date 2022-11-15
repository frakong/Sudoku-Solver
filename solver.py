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

print_sudoku_puzzle(sudoku_puzzle)
print(find_first_empty_space(sudoku_puzzle))