#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class HeuristiqueFinJeu():
    '''
    Heuristique appellée en fin de partie.
    Le but est de contrôler les zones vides les plus grosses possibles, on associe donc un score grand à ces dernières
    '''
    def __init__(self, board, color):
        self._myboard = board
        self._mycolor = color
        #self._first_line = [self._myboard.flatten([1,m]) for m in range(1,10)]+ [self._myboard.flatten([9,m]) for m in range(1,10)] + [self._myboard.flatten([m,1]) for m in range(2,9)] + [self._myboard.flatten([m,9]) for m in range(2,9)]

    def evaluate(self):
        (black, white, others) = self._myboard._count_areas()
        if (self._mycolor == self._myboard._BLACK):
            return black*10
        else:
            return white*10

    '''
    def number_max_aligned(self, case):
        number = 1
        already_browsed = []
        moved_case = case
        allies = self.allied_neighbors(moved_case)
        while (( allies != []) and (allies[0] not in already_browsed) and (case not in self._first_line)):
            number += 1
            already_browsed.append(allies[0])
            moved_case = allies[0]
            allies = self.allied_neighbors(moved_case)
        if moved_case in self._first_line:
            return number*100
        else:
            return number*10
        
    def allied_neighbors(self, move):
        neighbors = self._myboard._get_neighbors(move)
        legal_moves = self._myboard.legal_moves()
        allies = []
        for case in neighbors:
            if case not in legal_moves:
                if (self._myboard.__getitem__(case) == self._mycolor):
                    allies.append(case)
        return allies
    '''