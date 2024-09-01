#!/usr/bin/python3
"""N Queens Puzzle Solver using a recursive generator approach."""

import sys


def queens(n, i=0, a=[], b=[], c=[]):
    """
    Recursive generator to find all possible solutions for the N Queens puzzle.

    Parameters:
        - n: Size of the chessboard (N x N).
        - i: Current row index being processed.
        - a: List storing the column positions of the placed queens.
        - b: List storing the sums of row and column indices
            (i + j) to track main diagonals.
        - c: List storing the differences of row and column indices
            (i - j) to track anti-diagonals.

    Yields:
        - A list representing a valid config of queens on the board.
    """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """
    Solves the N-Queens problem and prints all possible solutions.

    Parameters:
        - n: The size of the chessboard (N x N).

    Prints:
        - Each solution as a list of coordinates [row, col] for each queen.
    """
    for solution in queens(n):
        print([[i, solution[i]] for i in range(n)])


def main():
    """
    The main function to handle input and start the N-Queens solving process.

    Where:
        - N: The size of the chessboard (N x N), and must be an integer >= 4.

    Handles errors:
        - Prints usage info if the wrong number of arguments is provided.
        - Prints an error if N is not an integer.
        - Prints an error if N is less than 4.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve(n)


# if __name__ == "__main__":
#     main()
