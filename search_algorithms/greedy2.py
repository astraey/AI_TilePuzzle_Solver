#!/usr/bin/env python

import sys
from random import randint
import puzzle
import util
import copy


class GREEDY2:

    def __init__(self, puzzle):

        self.initialPuzzle = puzzle
        self.priorityQueue = util.PriorityQueue()

        #The priority queue retreives the element with the lowest value associated first, which in this case is the closest to the solution,
        #as it is based on the number of tiles in incorrect places
        self.priorityQueue.push(puzzle, self.sumDistancesTilesToCorrectPlaces(puzzle))
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

            legalMoves = board.legalMoves() 

            self.sumBranchingFactor += len(legalMoves)

            #We keep track of the expanded nodes
            self.nodesExpanded = self.nodesExpanded + 1

            #When expanding a board, if it's not the solution, we will automatically add it to our visited list. This way we make sure that 
            #the same board won't be expanded again.
            self.visited.append(board.returnCopy())

            for legalMove in legalMoves:
                aux = board.returnCopy()
                aux.doMove(legalMove)

                #If the board is not in the visited list, we push it into the priority queue
                if not aux.isInList(self.visited):
                    self.priorityQueue.push(aux, self.sumDistancesTilesToCorrectPlaces(aux))

                #If the board has been visited before, we simply drop the board



    #Returns the sum of the distances of every tile to its correct place
    def sumDistancesTilesToCorrectPlaces(self, board):

        result = 0

        count = 1

        for i in range(0,board.size):
            for j in range(0,board.size):
                if board.puzzle[i][j]!=(count%(board.size*board.size)):

                    wrongTile = board.puzzle[i][j]

                    #i and j are the current coordinates of the wrong tile 

                    countAux = 1

                    #We iterate over the matrix to find the right position of the tile
                    for y in range(0,board.size):
                        for z in range(0,board.size):
                            #Condition is true if it's the right position for the tile
                            if wrongTile == (countAux%(board.size*board.size)):
                                #abs(i - y) + abs(j - z) is the actual amount of movements that it takes to get from one position to the other
                                result = result + abs(i - y) + abs(j - z)

                            countAux+=1

                count+=1

        return result
