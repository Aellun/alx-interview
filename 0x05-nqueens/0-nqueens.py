#!/usr/bin/python3

'''The N queens puzzle is the challenge
    of placing N non-attacking queens on an N×N chessboard.
    Write a program that solves the N queens problem
'''

import sys


def is_safe(board, row, col, N):
    '''
    Check if a queen can be placed on board[row][col]
    without being attacked.

    Parameters:
        - board: 2D list representing the chessboard.
        - row: The row index where the queen is to be placed.
        - col: The column index where the queen is to be placed.
        - N: The size of the chessboard (N x N).

    Returns:
        - True if it's safe to place the queen,
        False otherwise.
    '''
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    '''
    Utilizes backtracking to solve the N-Queens problem.

    Parameters:
        - board: 2D list representing the chessboard.
        - col: Current column index to attempt to place a queen.
        - N: The size of the chessboard (N x N).
        - solutions: List to store all valid solutions found.
    Returns:
    - True if a solution is found, False otherwise.
    '''
    # Base case: If all queens are placed, store the solution
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    # Try placing the queen in all rows in the current column
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen
            board[i][col] = 1

            # Recur to place rest of the queens
            res = solve_nqueens_util(board, col + 1, N, solutions) or res

            # If placing the queen in the current row and column doesn't
            # lead to a solution, remove the queen (backtrack)
            board[i][col] = 0

    return res


def solve_nqueens(N):
    '''
    Initializes the chessboard and starts the N-Queens solving process.

    Parameters:
        - N: The size of the chessboard (N x N).

    Prints:
    - All possible solutions, where each solution is represented as a list
      of coordinates [row, col] for each queen.
    '''
    # Initialize the chessboard with 0s (no queens placed)
    board = [[0 for _ in range(N)] for _ in range(N)]

    # List to store solutions
    solutions = []

    # Start solving from the first column
    solve_nqueens_util(board, 0, N, solutions)

    # Print all the solutions found
    for solution in solutions:
        print(solution)


def main():
    '''
    The main function to handle input
    and start the N-Queens solving process.

    Where:
        - N: The size of the chessboard (N x N), and must be an integer >= 4.

    Handles errors:
        - Prints usage information if the wrong number
        of arguments is provided.
        - Prints an error if N is not an integer.
        - Prints an error if N is less than 4.
    '''
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if the provided argument is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-Queens problem
    solve_nqueens(N)


if __name__ == "__main__":
    main()
