#!/usr/bin/env python

import sys
from random import randint
import puzzle
import util
import copy


class BFS:

    def __init__(self, puzzle):


        self.initialPuzzle = puzzle
        self.queue = util.Queue()
        self.queue.push(puzzle)
        self.foundSolution = False
        self.nodesExpanded = 0
        self.sumBranchingFactor = 0

    def solvePuzzle(self):

        while not self.queue.isEmpty() and not self.foundSolution:
            targetBoard = self.queue.pop()
            #print "\nThis is the initial puzzle"
            #targetBoard.printPuzzle()
            #print "\n"
            self.expandBoard(targetBoard)

    
    def expandBoard(self, board):

        if board.checkPuzzle():
            self.foundSolution = True
            print "Expanded Nodes: "+ str(self.nodesExpanded)
            if self.nodesExpanded != 0:
                averageBranchingFactor = (self.sumBranchingFactor / float(self.nodesExpanded))
                print "Average Branching Factor: %.2f" % averageBranchingFactor
            else:
                print "Average Branching Factor: "+str(self.sumBranchingFactor)
        else:

            legalMoves = board.legalMoves()
            self.nodesExpanded = self.nodesExpanded + 1
            self.sumBranchingFactor += len(legalMoves)
            
            for legalMove in legalMoves:
                aux = board.returnCopy()
                aux.doMove(legalMove)
                self.queue.push(aux)

