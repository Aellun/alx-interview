#!/usr/bin/python3
'''N Queens Puzzle Solver using a recursive generator approach'''
import sys


def generate_solutions(row, column):
    '''Generate all valid solutions
    for placing N queens on an N x N chessboard.
    Args:
        row (int): The number of rows (and queens) to place.
        column (int): The number of columns on the chessboard.

    Returns:
        list: A list of lists, where each inner list represents
        a valid arrangement of queens.'''
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    '''Place a queen in a safe position on the chessboard.
    Args:
        queen (int): The current queen's row index.
        column (int): The number of columns on the chessboard.
        prev_solution (list): The previous valid
        positions of queens.

    Returns:
        list: A list of new valid positions
        with the current queen placed.'''
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    '''Check if placing a queen at (q, x) is safe.

    Args:
        q (int): The current queen's row index.
        x (int): The column index where the queen is to be placed.
        array (list): The current arrangement of queens.

    Returns:
        bool: True if the position is safe, False otherwise.'''
    if x in array:
        return (False)
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def init():
    '''initializes the program at CLI'''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def n_queens():
    '''Main function to solve the N Queens
    challenge and print the solutions'''
    n = init()
    # generate all solutions
    solutions = generate_solutions(n, n)
    # print solutions
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()
