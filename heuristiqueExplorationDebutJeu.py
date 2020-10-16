#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class HeuristiqueExplorationDebutJeu():
    '''
    Heuristique d'exploration de début de partie.
    La stratégie initiale est de jouer uniquement sur les 3 et 4e ligne du plateau.
    Si possible, on ne joue pas à côté d'un pion dans ses voisins.
    '''
    def __init__(self, board, move, neighbors):
        self._myboard = board
        self._mymove = move
        self._third_line = [self._myboard.flatten([2,m]) for m in range(2,7)] + [self._myboard.flatten([6,m]) for m in range(2,7)] + [self._myboard.flatten([m,2]) for m in range(3,6)] + [self._myboard.flatten([m,6]) for m in range(3,6)]
        self._fourth_line = [self._myboard.flatten([3,m]) for m in range(3,6)] + [self._myboard.flatten([5,m]) for m in range(3,6)] + [self._myboard.flatten([4,3])] + [self._myboard.flatten([4,5])]
        self._neighbors = neighbors

    def evaluate(self):
        is_interesting = True

        if (self._mymove not in self._third_line) and (self._mymove not in self._fourth_line):
            is_interesting = False
            return is_interesting

        for i in self._neighbors:
            if i not in self._myboard.legal_moves():
                is_interesting = False
                return is_interesting

        return is_interesting
