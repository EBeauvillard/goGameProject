# -*- coding: utf-8 -*-
''' This is the file you have to modify for the tournament. Your default AI player must be called by this module, in the
myPlayer class.

Right now, this class contains the copy of the randomPlayer. But you have to change this!
'''

import time
import Goban
from random import choice
from playerInterface import *
import FirstMoves
import MinMax
import AlphaBeta

class myPlayer(PlayerInterface):
    ''' Example of a random player for the go. The only tricky part is to be able to handle
    the internal representation of moves given by legal_moves() and used by push() and
    to translate them to the GO-move strings "A1", ..., "J8", "PASS". Easy!

    '''
    # New here: _current_board is the list of played moves during the whole game {list[str]}
    # New here: memo_legal_moves will be equal to legal_move at turn n-1 (list{str}),
    # it is initialised in __init__
    _current_board = []
    _memo_legal_moves = []

    def __init__(self):
        self._board = Goban.Board()
        self._mycolor = None
        self.memo_legal_moves = [self._board.move_to_str(m) for m in self._board.legal_moves()]

    def getPlayerName(self):
        return "Gwenaëlle"

    def getPlayerMove(self):
        # New here: trigger helps to know which strategy has to be used this turn
        trigger = 1

        # New here: update of current_board with the play our adversary just did,
        #           memo_legal_moves is also updated
        legals = [self._board.move_to_str(m) for m in self._board.legal_moves()]
        for k in range(len(self._memo_legal_moves)):
            if (self._memo_legal_moves[k] not in legals) and (self ._memo_legal_moves[k] not in self._current_board):
                self._current_board.append(self._memo_legal_moves[k])
        self._memo_legal_moves = legals


        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return "PASS"


        if len(self._current_board) <= 10:

            strategie = FirstMoves.firstMoves(self._board, self._current_board, self._mycolor)
            move_name = strategie.start()
            # move_name = 0 if there is no board to copy
            if move_name:
                trigger = 0
                # move needs to be an internal representation here
                move = self._board.name_to_flat(move_name)

        # trigger = 0 only if the first moves strategy has been chosen
        if trigger:
            #strategie = MinMax.minMax(self._mycolor, self._board)
            strategie = AlphaBeta.alphaBeta(self._mycolor, self._board)
            move = strategie.bestMove()

        # New here: update of played_moves with the play our player is about to do.
        #           flat_to_name needed to have a string added in current_board
        self._current_board.append(self._board.flat_to_name(move))

        self._board.push(move)
        # New here: allows to consider internal representations of moves
        print("I am playing ", self._board.move_to_str(move))
        print("My current board :")
        self._board.prettyPrint()
        # move is an internal representation. To communicate with the interface I need to change if to a string
        return Goban.Board.flat_to_name(move)

    def playOpponentMove(self, move):
        print("Opponent played ", move) # New here
        # the board needs an internal representation to push the move.  Not a string
        self._board.push(Goban.Board.name_to_flat(move))

    def newGame(self, color):
        self._mycolor = color
        self._opponent = Goban.Board.flip(color)

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")
