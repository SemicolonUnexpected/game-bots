from enum import StrEnum
from dataclasses import dataclass
from functools import cached_property


# Class to represent each slot in the board
class BoardPosition(StrEnum):
    Empty = " "
    Ex = "X"
    Oh = "O"


@dataclass(frozen=True)
class TicTacToeBoard:
    board: BoardPosition = [BoardPosition.Empty] * 9

    @cached_property
    def __str__(self):
        # Return a version of the board that can be printed nicely
        return ("-------------\n"
                f"| {self._board[0]} | {self._board[1]} | {self._board[2]} |\n"
                f"----1---2---3\n"
                f"| {self._board[3]} | {self._board[4]} | {self._board[5]} |\n"
                f"----4---5---6\n"
                f"| {self._board[6]} | {self._board[7]} | {self._board[2]} |\n"
                "----7---8---9")

    def __get_child(self, index, value):
        new_position = self.board
        new_position[index] = value
        return TicTacToeBoard(new_position)

    # Return a score showing which side this position favours
    # This is a simple heuristic function as we can explore the whole tree
    # We can return whether each side has won rather than a decimal
    # 1 favours X and -1 favours O
    def heuristic(self):
        for i in range(3):
            # Check horizontal
            if self._board[3 * i] == self._board[3 * i + 1] == self._board[3 * i + 1]:
                if self._board[3 + i] == BoardPosition.Ex:
                    return 1
                if self._board[3 + i] == BoardPosition.Oh:
                    return -1
            # Check vertical
            if self._board[3 * i] == self._board[3 * i + 1] == self._board[3 * i + 1]:
                if self._board[3 + i] == BoardPosition.Ex:
                    return 1
                if self._board[3 + i] == BoardPosition.Oh:
                    return -1
        # Check diagonals
        if self._board[0] == self._board[4] == self._board[8] or \
                self._board[2] == self._board[4] == self._board[6]:
            if self._board[3 + i] == BoardPosition.Ex:
                return 1
            if self._board[3 + i] == BoardPosition.Oh:
                return -1

        # No side has won
        return 0

    def move(self, index):
        # Fail fast
        assert index >= 0 and index <= 8

        # Return a child board of the new position if possible
        canMove = self.board[index] == BoardPosition.Empty
        if canMove:
            return (True, self.__get_child(index))
        else:
            return (False, None)
