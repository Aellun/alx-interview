#!/usr/bin/python3
""" calculates island parameters
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid

        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        Grid is rectangular, with its width and height not exceeding 100
        The grid is completely surrounded by water
        There is only one island (or nothing).
        The island doesn’t have “lakes”

    Parameters:
    grid (List[List[int]]): A rectangular grid (a list of lists),
    where 0 represents water and 1 represents land.

    Returns:
    int: The perimeter of the island. Each cell has a side length of 1.
         The grid is guaranteed to be surrounded by water and contains
         only one island with no lakes.

    """

    # Dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # Initialize perimeter count
    perimeter = 0

    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Check if the current cell is land
            if grid[r][c] == 1:
                # Check all four sides

                # Up
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                # Down
                if r == rows - 1 or grid[r+1][c] == 0:
                    perimeter += 1
                # Left
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                # Right
                if c == cols - 1 or grid[r][c+1] == 0:
                    perimeter += 1

    return perimeter
