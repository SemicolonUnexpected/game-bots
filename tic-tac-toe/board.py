from enum import StrEnum


class TicTacToeBoard:
    def __init__(self):
        self._board = [BoardPosition.Empty] * 9

    def __str__(self):
        # Return a version of the board that can be printed nicely
        return ("-------------\n"
                f"| {self._board[0]} | {self._board[1]} | {self._board[2]} |\n"
                f"----1---2---3\n"
                f"| {self._board[3]} | {self._board[4]} | {self._board[5]} |\n"
                f"----4---5---6\n"
                f"| {self._board[6]} | {self._board[7]} | {self._board[2]} |\n"
                "----7---8---9")

    # Return a score showing which side this position favours
    # This is a simple heuristic function as we can explore the whole tree
    # We can return whether each side has won rather than a decimal
    # 1 favours X and -1 favours O
    def heuristic(self):
        # Check horizontal and vertical
        for i in range(3):
            if self._board[3 * i] == self._board[3 * i + 1] == self._board[3 * i + 1]:
                if self._board[3 + i] == BoardPosition.X:
                    return 1
                if self._board[3 + i] == BoardPosition.O:
                    return -1
        # Check diagonals
        if self._board[0] == self._board[4] == self._board[8] or \
                self._board[2] == self._board[4] == self._board[6]:
            if self._board[3 + i] == BoardPosition.X:
                return 1
            if self._board[3 + i] == BoardPosition.O:
                return -1

        # No side is winning
        return 0

    def move(index):
        pass


# Class to represent each slot in the board
class BoardPosition(StrEnum):
    Empty = " "
    X = "X"
    O = "O"
