import clr
clr.AddReference("Sudoku.Shared")
clr.AddReference("Sudoku.RecuitSolver")
from Sudoku.Z3Solvers import Z3SubstitutionsSolver
netSolver = Z3SubstitutionsSolver()
solvedSudoku = netSolver.Solve(sudoku)