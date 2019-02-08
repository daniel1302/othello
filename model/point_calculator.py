from array import *
from . import game_board

class point_calculator:

    def __init__(self, board, x, y, pawn_color):
        self.board = board
        self.active = set()
        self.x = x
        self.y = y
        self.pawn_color = pawn_color

        self.score = self._calculate_score(x, y, pawn_color)

    def _calculate_score(self, x, y, pawn_color):
        return sum([
            int(self._in_line_up()),
            int(self._in_line_down()),
            int(self._in_line_left()),
            int(self._in_line_right()),
            int(self._in_line_up_right()),
            int(self._in_line_down_right()),
            int(self._in_line_up_left()),
            int(self._in_line_down_left())
        ])


    def get_move(self):
        return (self.x, self.y)


    def get_score(self):
        return self.score


    def get_active(self):
        return self.active


    def is_move_possible(self):
        return self.score > 0


    def _in_line_up(self):
        return self._calculate_points(lambda x, dx: x, lambda y, dy: y - dy)


    def _in_line_down(self):
        return self._calculate_points(lambda x, dx: x, lambda y, dy: y + dy)


    def _in_line_left(self):
        return self._calculate_points(lambda x, dx: x - dx, lambda y, dy: y)


    def _in_line_right(self):
        return self._calculate_points(lambda x, dx: x + dx, lambda y, dy: y)


    def _in_line_up_right(self):
        return self._calculate_points(lambda x, dx: x + dx, lambda y, dy: y - dy)


    def _in_line_down_right(self):
        return self._calculate_points(lambda x, dx: x - dx, lambda y, dy: y + dy)


    def _in_line_up_left(self):
        return self._calculate_points(lambda x, dx: x - dx, lambda y, dy: y - dy)


    def _in_line_down_left(self):
        return self._calculate_points(lambda x, dx: x + dx, lambda y, dy: y + dy)


    def _calculate_points(self, dx, dy):
        points = 0

        _active = set()

        max = len(self.board) - 1
        for i in range(1, max):
            _x = dx(self.x, i)
            _y = dy(self.y, i)

            if _x < 1 or _x > max or _y < 1 or _y > max:
                return False

            if self.board[_x][_y] == game_board.FIELD_EMPTY():
                return False

            if points > 0 and self.board[_x][_y] == self.pawn_color:
                self.active |= _active

                return points

            if self.board[_x][_y] == game_board.OPPOSITE_PAWN(self.pawn_color):
                _active.add((_x, _y))
                points += 1

        return False




