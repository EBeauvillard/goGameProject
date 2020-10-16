#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heuristiqueZero

class minMax():
        ''' 
        Stratégie du MinMax sans implémentation particulière
        
        '''

    def __init__(self, color, board):
        self._mycolor = color
        self._myboard = board

    def maxMin(self, depth):
        if (self._myboard.is_game_over() or (depth == 0)):
            evaluate = heuristiqueZero.HeuristiqueZero(self._myboard, self._mycolor)
            return (evaluate.evaluate(), -1)
        else:
            best = - 100000
            moves = self._myboard.legal_moves()
            bestmove = -1
            for move in moves:
                self._myboard.push(move)
                prec = best
                (score, place) = self.minMax(depth - 1)
                best = max(best, score)
                if (prec < best):
                    bestmove = move
                self._myboard.pop()
            return (best,bestmove)

    def minMax(self, depth):
        if (self._myboard.is_game_over() or (depth == 0)):
            evaluate = heuristiqueZero.HeuristiqueZero(self._myboard, self._mycolor)
            return (evaluate.evaluate(), -1)
        else:
            worst = + 100000
            moves = self._myboard.legal_moves()
            worstmove = -1
            for move in moves:
                self._myboard.push(move)
                prec = worst
                (score, place) = self.maxMin(depth - 1)
                worst = min(worst, score)
                if (prec < worst):
                    worstmove = move
                self._myboard.pop()
            return (worst,worstmove)

    def bestMove(self, depth):
        best,move = self.maxMin(depth)
        return move
