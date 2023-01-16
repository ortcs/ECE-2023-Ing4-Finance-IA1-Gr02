import clr
clr.AddReference("Sudoku.Shared")
clr.AddReference("Sudoku.SodukuRecuitSolver")
from Sudoku.RecuitSolver import SudokuRecuitSolver
netSolver = SudokuRecuitSolver()
solvedSudoku = netSolver.Solve(sudoku)