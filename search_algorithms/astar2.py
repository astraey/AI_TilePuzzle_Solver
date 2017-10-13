#!/usr/bin/env python

import sys
from random import randint
import puzzle
import util
import copy


class ASTAR2:

    def __init__(self, puzzle):

        self.initialPuzzle = puzzle
        self.priorityQueue = util.PriorityQueue()

        self.priorityQueue.push(puzzle, self.sumDistancesTilesToCorrectPlaces(puzzle) + puzzle.depth)
        self.foundSolution = False
        self.nodesExpanded = 0
        self.sumBranchingFactor = 0

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
            self.visited.append(board.returnCopy())

            legalMoves = board.legalMoves()  

            #We keep track of the number of expanded nodes
            self.nodesExpanded = self.nodesExpanded + 1
            self.sumBranchingFactor += len(legalMoves)

            for legalMove in legalMoves:
                aux = board.returnCopy()
                aux.doMove(legalMove)
                aux.depth += 1

                #If the board is not in the visited list, we push it into the priority queue, adding its depth to the total estimated cost and
                #the sum of distances to their correct positions as the priority value for the queue
                if not aux.isInList(self.visited):
                    self.priorityQueue.push(aux, self.sumDistancesTilesToCorrectPlaces(aux) + aux.depth)

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
