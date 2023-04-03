#!/usr/bin/python3

import sys


def print_solution(board):
    """Prints a solution to the N queens problem."""
    for row in board:
        print(" ".join(str(cell) for cell in row))


def is_safe(board, row, col):
    """Checks if a queen can be placed in a given position."""
    # Check the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col):
    """Solves the N queens problem using backtracking."""
    if col >= len(board):
        # All queens have been placed, print the solution
        print_solution(board)
        return True

    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1

            # Recursively try to place the rest of the queens
            solve_n_queens(board, col + 1)

            board[row][col] = 0

    return False


def n_queens(n):
    """Solves the N queens problem."""
    if not isinstance(n, int):
        print("N must be a number")
        return 1

    if n < 4:
        print("N must be at least 4")
        return 1

    # Initialize the chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]

    solve_n_queens(board, 0)

    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    exit_code = n_queens(n)
    sys.exit(exit_code)
