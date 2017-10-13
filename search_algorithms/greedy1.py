#!/usr/bin/env python

import sys
from random import randint
import puzzle
import util
import copy


class GREEDY1:

    def __init__(self, puzzle):


        self.initialPuzzle = puzzle
        self.priorityQueue = util.PriorityQueue()

        #The priority queue retreives the element with the lowest value associated first, which in this case is the closest to the solution,
        #as it is based on the number of tiles in incorrect places
        self.priorityQueue.push(puzzle, self.tilesInIncorrectPlaces(puzzle))
        self.foundSolution = False
        self.nodesExpanded = 0
        self.sumBranchingFactor = 0


        #List where we save the boards that we have expanded
        #In many cases, the priority queue would always choose a pair of boards and those two and only those two would keep being expanded
        #This is an efective way of solving the loop problem, as we can make sure that we will never get stuck in a loop. 
        self.visited = []

    def solvePuzzle(self):

        while not self.priorityQueue.isEmpty() and not self.foundSolution:
            targetBoard = self.priorityQueue.pop()
            self.expandBoard(targetBoard)
    
    def expandBoard(self, board):

        if board.checkPuzzle():
            self.foundSolution = True
            print "Found Solution"
            print "Expanded Nodes: "+ str(self.nodesExpanded)
            if self.nodesExpanded != 0:
                averageBranchingFactor = (self.sumBranchingFactor / float(self.nodesExpanded))
                print "Average Branching Factor: %.2f" % averageBranchingFactor
            else:
                print "Average Branching Factor: "+str(self.sumBranchingFactor)

        else:
            
            #When expanding a board, if it's not the solution, we will automatically add it to our visited list. This way we make sure that 
            #the same board won't be expanded again.

            legalMoves = board.legalMoves()

            self.sumBranchingFactor += len(legalMoves)
            self.visited.append(board.returnCopy())

            #We keep track of the expanded nodes
            self.nodesExpanded = self.nodesExpanded + 1
     
            for legalMove in legalMoves:
                aux = board.returnCopy()
                aux.doMove(legalMove)

                #If the board is not in the visited list, we push it into the priority queue
                if not aux.isInList(self.visited):
                    self.priorityQueue.push(aux, self.tilesInIncorrectPlaces(aux))

                #If the board has been visited before, we simply drop the board



    #Returns the number of tiles in an incorrect place
    def tilesInIncorrectPlaces(self, board):

        noTilesIncorrectPlaces = 0
        count = 1

        for i in range(0,board.size):
            for j in range(0,board.size):
                if board.puzzle[i][j]!=(count%(board.size*board.size)):
                    noTilesIncorrectPlaces += 1
                count+=1

        return noTilesIncorrectPlaces

