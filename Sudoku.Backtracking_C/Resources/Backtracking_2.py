def solve_sudoku(board):
   empty = find_empty(board)
   if not empty:
       return True
   row, col = empty   for num in range(1,10):
       if is_valid(board, row, col, num):
           board[row][col] = num           if solve_sudoku(board):
               return True           board[row][col] = 0
   return Falsedef find_empty(board):
   for row in range(len(board)):
       for col in range(len(board[0])):
           if board[row][col] == 0:
               return (row, col)
   return Nonedef is_valid(board, row, col, num):
   for x in range(len(board)):
       if board[x][col] == num and row != x:
           return False
   for y in range(len(board[0])):
       if board[row][y] == num and col != y:
           return False
   x0, y0 = (row//3)*3, (col//3)*3
   for x in range(3):
       for y in range(3):
           if board[x0+x][y0+y] == num and (x0+x, y0+y) != (row, col):
               return False
   return Trueboard = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]solve_sudoku(board)
print(board)