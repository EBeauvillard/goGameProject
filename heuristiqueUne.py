#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class HeuristiqueZero():

    def __init__(self, board, color):
        self._board = board
        self._mycolor = color

    def evaluate(self):
        score = self._board._nbWHITE - self._board._nbBLACK
        if (self._mycolor == self._board._WHITE):
            return score
        else:
            return -score
