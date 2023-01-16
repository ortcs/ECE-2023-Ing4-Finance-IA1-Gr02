import clr
clr.AddReference("Sudoku.Shared")
clr.AddReference("Sudoku.SodukuRecuitSolver")
from Sudoku.RecuitSolver import RecuitSubstitutionsSolver
netSolver = RecuitSubstitutionsSolver()
solvedSudoku = netSolver.Solve(sudoku)