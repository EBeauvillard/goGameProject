# -*- coding: utf-8 -*-

import Goban
import json
import random as rd


'''Ouvre le fichier json et stocke les données dans la liste de dictionnaires
   data_dict'''
with open('games.json') as json_data:
    data_dict = json.load(json_data)

class firstMoves():

    def __init__(self, board, current_board, color):
        self._board = board
        self._current_board = current_board
        self._mycolor = color

    '''Permet de transformer le format de couleur donné par Goban._board en format
    de couleur exploitable pour le dictionnaire provenant du .json.

       Argument: color {int}

       Retourne: {str}
    '''
    def changeTypeOfColor(self, color):
        if color == self._board._BLACK:
            return 'B'
        elif color == self._board._WHITE:
            return 'W'

    '''Première version : le joueur choisi aléatoirement une partie à copier parmi
       celles historiques

       Retourne: move {str}
    '''
    def start(self):

        # Table des indices des parties historiques correspondantes à la partie
        # actuellement jouée
        tab_ind=[]

        # Nombre de coups joués
        nb_moves = len(self._current_board)

        color = self.changeTypeOfColor(self._mycolor)

        for i in range (len(data_dict)):
            if ((data_dict[i]['winner'] == color) and (data_dict[i]['moves'][:nb_moves] == self._current_board)):
                tab_ind.append(i)

        #print("Indice(s) de(s) partie(s) copiable(s):",tab_ind)
        if (tab_ind == []):
            print("Pas de partie à copier")
            return 0

        random_nb = rd.randint(0, len(tab_ind) - 1)

        ind = tab_ind[random_nb]
        #print("Plateau actuel:",current_board)
        #print("Partie copiée:",data_dict[ind]['moves'])

        move = data_dict[ind]['moves'][nb_moves]
        #print("Coup suivant à jouer:",move)
        return move
