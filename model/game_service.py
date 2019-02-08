from array import *
from . import game_board
from .point_calculator import point_calculator
from .move_finder import move_finder

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

        # FOR TESTS
        # board[4][4] = game_board.PAWN_WHITE()
        # board[5][5] = game_board.PAWN_WHITE()
        # board[4][5] = game_board.PAWN_BLACK()
        # board[5][4] = game_board.PAWN_BLACK()
        # board[5][6] = game_board.PAWN_WHITE()
        # board[3][6] = game_board.PAWN_WHITE()
        # board[2][7] = game_board.PAWN_WHITE()
        # board[6][3] = game_board.PAWN_WHITE()
        # board[7][2] = game_board.PAWN_WHITE()
        # board[3][3] = game_board.PAWN_BLACK()
        # board[4][3] = game_board.PAWN_WHITE()
        # board[7][5] = game_board.PAWN_WHITE()
        # board[8][4] = game_board.PAWN_BLACK()


        return board

    def move(self, x, y):
        calc = point_calculator(self.board, x, y, game_board.PAWN_BLACK())

        if not calc.is_move_possible():
            return

        for item in calc.get_active():
            self.board[item[0]][item[1]] = game_board.PAWN_BLACK()

        mf = move_finder(self.board, game_board.PAWN_WHITE())

        if not mf.has_move():
            return

        the_best_move = mf.get_the_best_move()
        for item in the_best_move.get_active():
            self.board[item[0]][item[1]] = game_board.PAWN_WHITE()

        white_move = the_best_move.get_move()
        self.board[white_move[0]][white_move[1]] = game_board.PAWN_WHITE()

        return


    def get_board(self):
        return self.board

    def get_size(self):
        return [self.width, self.height]