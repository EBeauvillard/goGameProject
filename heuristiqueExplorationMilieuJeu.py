#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class HeuristiqueExplorationMilieuJeu():
    '''
    Heuristique d'exploration de milieu de partie.
    La stratégie est de jouer uniquement à côté de pions déjà joués
    '''

    def __init__(self, board, move, neighbors):
        self._myboard = board
        self._mymove = move
        self._neighbors = neighbors

    def evaluate(self):
        is_interesting = False

        for i in self._neighbors:
            if (self._myboard.__getitem__(i) != self._myboard._EMPTY):
                is_interesting = True
                return is_interesting

        return is_interesting
