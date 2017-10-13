#!/usr/bin/env python

import sys
from random import randint
import puzzle
import util
import copy


class DFS:

    def __init__(self, puzzle):


        self.initialPuzzle = puzzle
        self.stack = util.Stack()
        self.stack.push(puzzle)
        self.foundSolution = False
        self.nodesExpanded = 0
        self.sumBranchingFactor = 0


    def solvePuzzle(self):

        while not self.stack.isEmpty() and not self.foundSolution:
            targetBoard = self.stack.pop()
            #print "\nThis is the initial puzzle"
            #targetBoard.printPuzzle()
            #print "\n"
            self.expandBoard(targetBoard)

    
    def expandBoard(self, board):

        self.nodesExpanded = self.nodesExpanded + 1

        if board.checkPuzzle():
            self.foundSolution = True
            print "Found Solution: "
            board.printPuzzle()
            print "Expanded Nodes: "+ str(self.nodesExpanded)

        else: 

            legalMoves = board.legalMoves()       
            for legalMove in legalMoves:
                aux = board.returnCopy()
                aux.doMove(legalMove)
                self.stack.push(aux)
