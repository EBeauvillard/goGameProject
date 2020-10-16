#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class HeuristiqueExplorationFinJeu():
    '''
    Heuristique d'exploration de fin de partie.
    La stratégie finale est de jouer uniquement sur les voisins de ses propres pions afin de fermer des zones de contrôle.
    '''

    def __init__(self, board, move, neighbors):
        self._myboard = board
        self._mymove = move
        self._neighbors = neighbors

    def evaluate(self):
        is_interesting = False

        for i in self._neighbors:
            if ((self._myboard.__getitem__(i) != self._myboard.next_player()) and (self._myboard.__getitem__(i) != self._myboard._EMPTY)) :
                is_interesting = True
                return is_interesting

        return is_interesting
