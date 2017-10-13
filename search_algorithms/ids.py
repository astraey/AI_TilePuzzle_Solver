#!/usr/bin/env python

import sys
from random import randint
import puzzle
import util
import copy


class IDS:

    def __init__(self, puzzle):

        self.initialPuzzle = puzzle
        self.stack = util.Stack()
        self.stack.push(puzzle)
        self.foundSolution = False
        self.nodesExpanded = 0
        self.sumBranchingFactor = 0
        self.depth = 0


    def solvePuzzle(self):

        while not self.foundSolution:
            
            #When the stack is empty, we reinsert the initial puzzle and restart the DFS, increasing the depth by one
            if self.stack.isEmpty():
                self.stack.push(self.initialPuzzle)
                self.depth = self.depth + 1
                print "Depth has ben increased to "+str(self.depth)

            targetBoard = self.stack.pop()
            #print "\nThis is the initial puzzle"
            #targetBoard.printPuzzle()
            #print "\n"
            self.expandBoard(targetBoard)

    
    def expandBoard(self, board):

        if board.checkPuzzle():
            self.foundSolution = True
            print "Found Solution: "
            board.printPuzzle()
            print "Expanded Nodes: "+ str(self.nodesExpanded)
            if self.nodesExpanded != 0:
                averageBranchingFactor = (self.sumBranchingFactor / float(self.nodesExpanded))
                print "Average Branching Factor: %.2f" % averageBranchingFactor
            else:
                print "Average Branching Factor: "+str(self.sumBranchingFactor)

        elif board.depth <= self.depth:

            legalMoves = board.legalMoves()    
            self.nodesExpanded = self.nodesExpanded + 1
            self.sumBranchingFactor += len(legalMoves)
               
            for legalMove in legalMoves:
                aux = board.returnCopy()
                aux.doMove(legalMove)
                aux.depth = aux.depth + 1
                self.stack.push(aux)

        #If the depth of the board in the search tree is bigger than the algorithm's depth, the node is simply dropped. 
        #It will be expanded in the next iteration
