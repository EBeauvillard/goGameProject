#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heuristiqueZero
import heuristiqueMilieuJeu
import heuristiqueFinJeu
import heuristiqueExplorationDebutJeu
import heuristiqueExplorationMilieuJeu
import heuristiqueExplorationFinJeu

class alphaBeta():
    ''' 
    Stratégie d'alpha-beta avec elagage
    Toutes les heuristiques appellées sont contenues dans d'autres fichiers et importées ici.
    Les Heuristiques dites "classiques" sont appelées si le jeu est finit ou l'arbre d'exploration est arrivé à la profondeur maximale demandée.
    Les Heuristiques d'exploration sont appelées à chaque branche pour évaluer si le coup joué en vaut la peine (booléen renvoyé par evaluate()). 
     Dans le cas contraire, la branche n'est pas explorée.
    La profondeur de l'arbre exploré dépend dans quelle moment de la partie nous sommes, comme indiqué dans la méthode depth.
    '''
    
    def __init__(self, color, board):
        self._mycolor = color
        self._myboard = board
        self._nbmoves = (self._myboard._BOARDSIZE)**2 - len(self._myboard.legal_moves()) + 1
        self._top_line = [self._myboard.flatten([m,9]) for m in range(1,10)]
        self._bot_line = [self._myboard.flatten([m,1]) for m in range(1,10)]
        self._left_line = [self._myboard.flatten([1,m]) for m in range(1,10)]
        self._right_line = [self._myboard.flatten([9,m]) for m in range(1,10)]
        self._depth = self.depth()

    def maxValue(self, depth, alpha, beta, lastmove, lastlastmove):
        if (self._myboard.is_game_over() or (depth == 0)):
            if (self._nbmoves <= 10):
                evaluate = heuristiqueZero.HeuristiqueZero(self._myboard, self._mycolor)
            elif (self._nbmoves <= 25):
                    evaluate = heuristiqueMilieuJeu.HeuristiqueMilieuJeu(self._myboard, self._mycolor, lastmove, lastlastmove)
            else:
                evaluate = heuristiqueFinJeu.HeuristiqueFinJeu(self._myboard, self._mycolor)
            return (evaluate.evaluate(), -1)
        else:
            moves = self._myboard.legal_moves()
            bestmove = -1
            for move in moves:
                neighbors = self.getAllNeighbors(move)
                if (self._nbmoves <= 10):
                    evaluate = heuristiqueExplorationDebutJeu.HeuristiqueExplorationDebutJeu(self._myboard, move, neighbors)
                elif (self._nbmoves <= 25):
                    evaluate = heuristiqueExplorationMilieuJeu.HeuristiqueExplorationMilieuJeu(self._myboard, move, neighbors)
                else:
                    evaluate = heuristiqueExplorationFinJeu.HeuristiqueExplorationFinJeu(self._myboard, move, neighbors)
                if (evaluate.evaluate()):
                    #print("Hééé mais ce coup là est SUPER intéressant" + str(move))
                    prec = alpha
                    self._myboard.push(move)
                    self._nbmoves += 1
                    (score, place) = self.minValue(depth - 1, alpha, beta, move, lastmove)
                    alpha = max(alpha, score)
                    if (beta <= alpha):
                        bestmove = move
                        self._myboard.pop()
                        self._nbmoves -=1
                        return (beta, bestmove)
                    if (alpha > prec):
                        bestmove = move
                    self._nbmoves -= 1
                    self._myboard.pop()
            return (alpha,bestmove)

    def minValue(self, depth, alpha, beta, lastmove, lastlastmove):
        if (self._myboard.is_game_over() or (depth == 0)):
            if (self._nbmoves <= 10):
                evaluate = heuristiqueZero.HeuristiqueZero(self._myboard, self._mycolor)
            elif (self._nbmoves <= 25):
                evaluate = heuristiqueMilieuJeu.HeuristiqueMilieuJeu(self._myboard, self._mycolor, lastmove, lastlastmove)
            else:
                evaluate = heuristiqueFinJeu.HeuristiqueFinJeu(self._myboard, self._mycolor)
            return (evaluate.evaluate(), -1)
        else:
            moves = self._myboard.legal_moves()
            worstmove = -1
            for move in moves:
                neighbors = self.getAllNeighbors(move)
                if (self._nbmoves <= 10):
                    evaluate = heuristiqueExplorationDebutJeu.HeuristiqueExplorationDebutJeu(self._myboard, move, neighbors)
                elif (self._nbmoves <= 25):
                    evaluate = heuristiqueExplorationMilieuJeu.HeuristiqueExplorationMilieuJeu(self._myboard, move, neighbors)
                else:
                    evaluate = heuristiqueExplorationFinJeu.HeuristiqueExplorationFinJeu(self._myboard, move, neighbors)
                if (evaluate.evaluate()):
                    #print("Hééé mais ce coup là est SUPER intéressant" + str(move))
                    prec = beta
                    self._myboard.push(move)
                    self._nbmoves += 1
                    (score, place) = self.maxValue(depth - 1, alpha, beta, move, lastmove)
                    beta = min(beta, score)
                    if (beta <= alpha):
                        bestmove = move
                        self._myboard.pop()
                        self._nbmoves -=1
                        return (alpha, bestmove)
                    if (prec > beta):
                        worstmove = move
                    self._nbmoves -= 1
                    self._myboard.pop()
            return (beta,worstmove)

    def bestMove(self):
        best,move = self.maxValue(self._depth, -1000000, 1000000, -1, -1)
        return move
    
    def getAllNeighbors(self, move):
        '''
        Renvoie en plus des voisins classiques les voisins diagonaux
        '''
        
        neighbors = self._myboard._get_neighbors(move)
        length = len(neighbors)
        if (length>1):
            if (length == 4):
                neighbors.append(max(neighbors) - 1)
                neighbors.append(max(neighbors) + 1)
                neighbors.append(min(neighbors) + 1)
                neighbors.append(min(neighbors) - 1)
            elif (length == 3):
                if (move in self._top_line):
                    neighbors.append(min(neighbors) + 1)
                    neighbors.append(min(neighbors) - 1)
                elif (move in self._bot_line):
                    neighbors.append(max(neighbors) - 1)
                    neighbors.append(max(neighbors) + 1)
                elif (move in self._left_line):
                    neighbors.append(max(neighbors) + 1)
                    neighbors.append(min(neighbors) + 1)
                else:
                    neighbors.append(max(neighbors) - 1)
                    neighbors.append(min(neighbors) - 1)
            else:
                if ((move in self._top_line) and (move in self._right_line)):
                    neighbors.append(min(neighbors) - 1)
                elif ((move in self._top_line) and (move in self._left_line)):
                    neighbors.append(min(neighbors) + 1)
                elif ((move in self._bot_line) and (move in self._left_line)):
                    neighbors.append(max(neighbors) + 1)
                else:
                    neighbors.append(max(neighbors) - 1)
        return neighbors
    
    def depth(self):
        if (self._nbmoves <= 10):
            return 2
        elif (self._nbmoves <= 25):
            return 3
        else:
            return 4
        
