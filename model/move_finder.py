from array import *
from . import game_board
from .point_calculator import point_calculator

class move_finder:
    def __init__(self, board, pawn_color):
        self.board = board
        self.pawn_color = pawn_color

        self.actions = []

        self._calculate_actions()


    def get_actions(self):
        return self.actions


    def get_the_best_move(self):
        if (len(self.actions) < 1):
            return None

        tmp = self.actions[0]

        for calc in self.actions:
            if tmp.get_score() < calc.get_score():
                tmp = calc

        return tmp

    def has_move(self):
        return len(self.actions) > 0

    def _calculate_actions(self):
        for x in range(len(self.board)-1):
            for y in range(len(self.board[x])-1):
                if self.board[x][y] != game_board.FIELD_EMPTY():
                    continue

                calc = point_calculator(self.board, x, y, self.pawn_color)

                if not calc.is_move_possible():
                    continue

                self.actions.append(calc)
