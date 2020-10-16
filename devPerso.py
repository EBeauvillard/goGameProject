#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Goban

def test():

    #third_line = [Goban.Board.flatten([1,m]) for m in range(3)]
    third_line = [Goban.Board.coord_to_name([2,m]) for m in range(2,7)]
    third_line +=[Goban.Board.coord_to_name([6,m]) for m in range(2,7)]
    third_line +=[Goban.Board.coord_to_name([m,2]) for m in range(3,6)]
    third_line +=[Goban.Board.coord_to_name([m,6]) for m in range(3,6)]

    fourth_line =[Goban.Board.coord_to_name([3,m]) for m in range(3,6)]
    fourth_line +=[Goban.Board.coord_to_name([5,m]) for m in range(3,6)]
    fourth_line +=[Goban.Board.coord_to_name([4,3])]
    fourth_line +=[Goban.Board.coord_to_name([4,5])]

    return fourth_line

print(test())
