from array import *
from . import game_board

class game_service:

    def __init__(self, width: int, height: int, board:list =None):
        self.width = width
        self.height = height

        self.board = (board, self.init_game())[board is None]


    def init_game(self):
        """
        Method to generate begining state of game board
        """
        board = []

        for x in range(self.width):
            board.append([])
            for y in range(self.height):
                board[x].append(game_board.FIELD_EMPTY())

        x = int(self.width/2)-1
        y = int(self.height/2)-1

        board[x][y] = game_board.PAWN_WHITE()
        board[x+1][y+1] = game_board.PAWN_WHITE()
        board[x][y+1] = game_board.PAWN_BLACK()
        board[x+1][y] = game_board.PAWN_BLACK()

        return board

    def move(self, x, y):

        return "OK"

    def get_board(self):
        return self.board

    def get_size(self):
        return [self.width, self.height]