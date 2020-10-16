Goban.py 
---------

Fichier contenant les règles du jeu de GO avec les fonctions et méthodes pour parcourir (relativement) efficacement
l'arbre de jeu, à l'aide de legal_moves() et push()/pop() comme vu en cours.

Ce fichier sera utilisé comme arbitre dans le tournoi. Vous avez maintenant les fonctions de score implantés dedans.
Sauf problème, ce sera la methode result() qui donnera la vainqueur quand is_game_over() sera Vrai.

Vous avez un décompte plus précis de la victoire dans final_go_score()

Pour vous aider à parcourir le plateau de jeu, si b est un Board(), vous pouvez avoir accès à la couleur de la pierre
posée en (x,y) en utilisant b[Board.flatten((x,y))]


GnuGo.py
--------

Fichier contenant un ensemble de fonctions pour communiquer avec gnugo


starter-go.py
-------------

Exemples de deux développements aléatoires (utilisant legal_moves et push/pop). Le premier utilise legal_moves et le
second weak_legal_moves, qui ne garanti plus que le coup aléatoire soit vraiment légal (à cause des Ko).

La première chose à faire est probablement de 


localGame.py
------------

Permet de lancer un match de myPlayer contre lui même, en vérifiant les coups avec une instanciation de Goban.py comme
arbitre. Vous ne devez pas modifier ce fichier pour qu'il fonctionne, sans quoi je risque d'avoir des problèmes pour
faire entrer votre IA dans le tournoi.


playerInterface.py
------------------

Classe abstraite, décrite dans le sujet, permettant à votre joueur d'implanter correctement les fonctions pour être
utilisé dans localGame et donc, dans le tournoi. Attention, il faut bien faire attention aux coups internes dans Goban
(appelés "flat") et qui sont utilisés dans legal_moves/weak_legal_moves et push/pop des coups externes qui sont
utilisés dans l'interface (les named moves). En interne, un coup est un indice dans un tableau 1 dimension
-1, 0.._BOARDSIZE^2 et en externe (dans cette interface) les coups sont des chaines de caractères dans "A1", ..., "J9",
"PASS". Il ne faut pas se mélanger les pinceaux.


myPlayer.py
-----------

Fichier que vous devrez modifier pour y mettre votre IA pour le tournoi. En l'état actuel, il contient la copie du
joueur randomPlayer.py


randomPlayer.py
---------------

Un joueur aléatoire que vous pourrez conserver tel quel


gnugoPlayer.py
--------------

Un joueur basé sur gnugo. Vous permet de vous mesurer à lui simplement.


namedGame.py
------------

Permet de lancer deux joueurs différents l'un contre l'autre.
Il attent en argument les deux modules des deux joueurs à importer.


MinMax.py
------------
Implémentation de la stratégie de Minmax pour choisir le prochain coup à jouer.


AlphaBeta.py
------------
Implémentation de la stratégie d'AlphaBeta pour choisir le prochain coup à jouer.


FirstMoves.py
------------
Implémentation du choix d'opening en fonction de la situation du plateau.

heuristiqueZero.py
------------
Heuristique d'évaluation de plateau comptant le nombre de pions.


heuristiqueMilieuJeu.py
------------
Heuristique d'évaluation de plateau comptant le nombre de pions capturés et la distance au dernier coup joué du prochain
coup.


heuristiqueFinJeu.py
------------
Heuristique d'évaluation de plateau comptant le nombre de zones capturés et leur surface.



heuristiqueExplorationDebutJeu.py
------------
Heuristique d'exploration enlevant de l'arbre les coups ni sur la 3e ou 4e ligne. Enlève de plus les coups à côté d'un 
voisin.


heuristiqueExplorationMilieuJeu.py
------------
Heuristique d'exploration enlevant les coups joués à côté de seulement des cases vides.


heuristiqueExplorationFinJeu.py
------------
Heuristique d'exploration enlevant les coups joués n'étant pas à côté de pions de sa propre couleur.


EXEMPLES DE LIGNES DE COMMANDES:
================================

python3 localGame.py
--> Va lancer un match myPlayer.py contre randomPlayer.py

python3 namedGame.py myPlayer randomPlayer
--> Va lancer un match entre votre joueur (NOIRS) et le randomPlayer
 (BLANC)

 python3 namedGame gnugoPlayer myPlayer
 --> gnugo (level 0) contre votre joueur (très dur à battre)
 
 
STRATEGIE D'IMPLEMENTATION DE LA STRATEGIE:
===========================================

Dès le début de notre réflexion, nous avions décidé de séparer nos stratégies de nos heuristiques et du reste de 
"myPlayer.py" pour avoir plus de visibilité. Ainsi nous avons mis en place un fichier/une classe pour chacune de nos
stratégies (MinMax et AlphaBeta) et de même pour chacune de nos heuristiques implémentées, qu'elles soient classiques
ou d'exploration.
De plus, cela nous permettait pour chacune des stratégies de pouvoir tester les différentes heuristiques que nous
implémenterions au fur et à mesure.

Suite à cela, le projet s'est découpé en 3 étapes.

La première était d'implémenter une vraie stratégie simple et qui fonctionne afin de nous familiariser avec le reste
des fonctions du projet. Nous avons donc implémenté un MinMax "bête et méchant", une bibliothèque d'ouverture basée
sur des parties partagées par notre professeur dans le projet, et une simple heuristique comptant les pions joués.

Une fois cela fait, la deuxième étape était d'améliorer chacune de ces méthodes.
Nous avons donc remplacé le MinMax par une exploration avec AlphaBeta. Nous avons de plus rajouté des heuristiques
d'exploration. A chaque nouvelle branche créée dans l'arbre d'exploration, ces heuristiques prennent en compte le plateau
et le coup joué. Elles renvoient un booléen indiquant si le coup joué est intéressant à explorer ou risque quoi qu'il
arrive d'être mauvais. Dans ce 2e cas, l'heuristique d'exploration a un rôle d'élagage et arrête l'exploration de l'arbre
pour ce coup-ci. Cela permet de diminuer grandement le temps de calcul.

Après cela implémenté, nous nous sommes rendus compte qu'afin d'améliorer notre joueur, il fallait être bien plus précis
sur notre heuristique d'évaluation qui était resté au point de départ du compte de nombre de pions, et qui considérait 
souvent tous ses coups possibles équivalents. Il jouait donc à chaque fois sur la première case du plateau libre, ce qui
n'était pas du tout intelligent.
Nous avons donc cherché à voir des stratégies de joueurs réels de go sur un plateau 9*9. Nous avons ainsi vu que le jeu
pouvait se découper en 3 phases différentes correspondant au début, milieu et fin de partie. Nous avons donc séparés nos
heuristiques classiques et d'exploration en 3 nouvelles heuristiques, qui chacune correspondrait à un moment de la partie.
Ainsi pour le début de partie, on cherche d'abord à être proche d'une partie de GO déja jouée de notre bibliothèque
d'opening. Ensuite, l'heuristique d'exploration ne fait jouer que sur la 3e et 4e ligne, l'heuristique d'évaluation compte
simplement le nombre de pions, car nous savions qu'après l'heuristique d'exploration la majeure partie de la stratégie de
début de jeu était faite.
Pour le milieu de jeu, l'heuristique d'exploration supprime tous les coups qui ne sont voisins qu'avec des cases vides.
Pour l'évaluation, on fait en sorte de maximiser les pions capturés et minimiser la distance du coup avec le dernier coup
joué. Néanmoins pour cette partie, le joueur joue en général la première case possible tout comme décrit dans la ligne 160
de ce readme. Nous n'avons pas eu le temps de chercher plus en avant pourquoi.
Pour la fin de jeu, nous avons décidé que la priorité était de "fermer" les zones vides contrôlées par un joueur. Ainsi,
l'exploration ne fait jouer que des coups à côté d'un pion de sa couleur, et l'évaluation maximise la taille des zones
vides contrôlées par un joueur.

Le temps de calcul étant satisfaisant avec cette stratégie de découpage en 3 parties, nous sommes restés sur cela. Nous
avons simplement changé la profondeur de l'arbre de recherche en fonction du moment de la partie. 2 au début car cela ne
change pas grand chose, 3 au milieu pour éviter d'avoir de trop gros calculs et 4 à la fin pour faire en sorte de bien
optimiser les captures de zones.
