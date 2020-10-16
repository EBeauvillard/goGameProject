#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt

class HeuristiqueMilieuJeu():
    '''
    Heuristique appelée en milieu de partie.
    Elle favorise la capture de pions et le fait de jouer proche du dernier pion joué.
    Nous n'avons pas réussi à trouver pourquoi mais dans l'état actuel elle ne favorise pas le fait de jouer proche du dernier pion joué.
    '''
    def __init__(self, board, color, move, lastmove):
        self._myboard = board
        self._mycolor = color
        self._move = move
        self._lastmove = lastmove
        #self._first_line = [self._myboard.flatten([1,m]) for m in range(1,10)]+ [self._myboard.flatten([9,m]) for m in range(1,10)] + [self._myboard.flatten([m,1]) for m in range(2,9)] + [self._myboard.flatten([m,9]) for m in range(2,9)]

    def evaluate(self):
        if (self._mycolor == self._myboard._BLACK):
            captured = self._myboard._capturedBLACK
        else:
            captured = self._myboard._capturedWHITE
        distance = self.distance(self._move, self._lastmove)
        return 5*captured - 5*distance
    
    def distance(self, move1, move2):
        '''
        Renvoie la partie entiere de la distance euclidienne entre move1 et move2
        '''
        if ((move1 != -1) and (move2 != -1)):
            x1, y1 = divmod(move1, self._myboard._BOARDSIZE)
            x2, y2 = divmod(move2, self._myboard._BOARDSIZE)
            dx = abs(x1 - y1)
            dy = abs(x2 - y2)
            return int(sqrt(dx**2 + dy**2))
        else:
            return 0