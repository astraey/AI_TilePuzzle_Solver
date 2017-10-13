#!/usr/bin/env python

import sys
from random import randint
import copy


class TilePuzzle:
	def __init__(self,size):
		self.size=size
		self.puzzle=[]
		self.zero=(0,0)
		self.moves=["U","D","L","R"]

		#Depth attribute in the search tree, for the algorithms that require it
		self.depth = 0

		#Inicialization of the puzzle
		count=1
		for i in range(0,size):
			self.puzzle.append([])
			for j in range(0,size):
				self.puzzle[i].append(count)
				count+=1

		#Define where the zero is. 
		self.puzzle[size-1][size-1]=0
		self.zero=(size-1,size-1)
	
	def readPuzzle(self,string):
		a=string.split(" ")
		count=0
		for i in range(0,self.size):
			for j in range(0,self.size):
				if int(a[count])==0:
					self.zero=(j,i)
				self.puzzle[j][i]=int(a[count])
				count+=1

	def checkPuzzle(self):
		count=1
		for i in range(0,self.size):
			for j in range(0,self.size):
				if self.puzzle[i][j]!=(count%(self.size*self.size)):
					return False
				count+=1
		return True

	
	def swap(self,(x1,y1),(x2,y2)):
		temp=self.puzzle[x1][y1]
		self.puzzle[x1][y1]=self.puzzle[x2][y2]
		self.puzzle[x2][y2]=temp

	def up(self):
		if (self.zero[0]!=0):
			self.swap((self.zero[0]-1,self.zero[1]),self.zero)
			self.zero=(self.zero[0]-1,self.zero[1])


	def down(self):
		if (self.zero[0]!=self.size-1):
			self.swap((self.zero[0]+1,self.zero[1]),self.zero)
			self.zero=(self.zero[0]+1,self.zero[1])


	def left(self):
		if (self.zero[1]!=0):
			self.swap((self.zero[0],self.zero[1]-1),self.zero)
			self.zero=(self.zero[0],self.zero[1]-1)


	def right(self):
		if (self.zero[1]!=self.size-1):
			self.swap((self.zero[0],self.zero[1]+1),self.zero)
			self.zero=(self.zero[0],self.zero[1]+1)
	
	def printPuzzle(self):
		for i in range(0,self.size):
			#Adding this print, the puzzle will be printed as a square
			print "\n"
			for j in range(0,self.size):
				print self.puzzle[i][j],

		print "\n\n"

	def doMove(self,move):
		if move=="U":
			self.up()
		if move=="D":
			self.down()
		if move=="L":
			self.left()
		if move=="R":
			self.right()
	
	def permute(self,numPerm):
		for i in range(0,numPerm):
			self.doMove(self.moves[randint(0,3)])
	
	def parseMoveSequence(self,string):
		for m in string:
			self.doMove(m)

	def legalMoves(self):

		returnValue = []
		
		if (self.zero[0]!=0):
			returnValue.append("U")

		if (self.zero[0]!=self.size-1):
			returnValue.append("D")

		if (self.zero[1]!=0):
			returnValue.append("L")

		if (self.zero[1]!=self.size-1):
			returnValue.append("R")

		return returnValue

	def returnCopy(self):
		return copy.deepcopy(self)

	def isInList(self, listBoards):

		for board in listBoards:
			
			if board.puzzle == self.puzzle:
				return True

		return False



			
		


