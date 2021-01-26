#Author: Keeton Martin
import numpy as np
import pandas as pd
import random

class Board():
	"""docstring for Board"""
	def __init__(self, size):
		self.size = size

		#Create a size x size empty array
		self.array = np.empty((3,3), dtype=str)

	def insertAtIndex(self, i, j, letter):
		# print(i, j)
		self.array[i][j] = letter

	def putX(self, howManyFromLeft, howManyFromTop):
		# print(self)
		# print("Col: ", howManyFromLeft, " Row: ", howManyFromTop)
		self.insertAtIndex(howManyFromTop, howManyFromLeft, "X")
		# print(self)
		# self.checkWinConditions("X")

	def putO(self, howManyFromLeft, howManyFromTop):
		# print(self)
		self.insertAtIndex(howManyFromTop, howManyFromLeft, "O")
		# print(self)
		self.checkWinConditions("O")

	def emptySpots(self):
		returnableSpots = []

		rowIndex = 0
		for row in self.array:
			colIndex = 0
			for spot in row:
				if not (spot == "X" or spot == "O"):
					returnableSpots.append((rowIndex, colIndex))
				colIndex+=1
			rowIndex+=1

		return returnableSpots

	def __str__(self):
		return str(self.array)

	def checkWinConditions(self, letter):
		if self.checkWonOnRow(letter) or self.checkWonOnCol(letter): # or self.checkWonOnDiag(letter):
			print("Game over! ", letter, " won the game. Play again!")
			exit()

	def checkWonOnRow(self, letter):
		"""
		"""
		won = False
		for i in range(self.size):
			countLetters = 0
			for j in range(self.size):
				if self.array[i][j] == letter:
					countLetters+=1
			if countLetters == 3:
				won = True
		return won

	def checkWonOnCol(self, letter):
		"""
		"""
		won = False
		for i in range(self.size):
			countLetters = 0
			for j in range(self.size):
				if self.array.T[i][j] == letter:
					countLetters += 1
			if countLetters == 3:
				won = True
		return won

	def checkWonOnDiag(self):
		pass

	def chooseBestXSpot(self):
		temp = self.playerCouldWin("X")
		temp2 = self.playerCouldWin("O")
		if temp:
			print("Winning!")
			return temp
		elif temp2:
			print("Almost missed it!")
			return temp2
		else:
			spotOptions = self.emptySpots()
			selectionTuple = random.choice(spotOptions)
			return selectionTuple[0],selectionTuple[1]

	def playerCouldWin(self, letter):
		rowIndex = 0
		for row in self.array:
			if (not otherLetter(letter) in row) and twoOccurences(letter, row):
				# return True
				targetCol = self.findWinningSpot(letter, row)
				return rowIndex, targetCol
			rowIndex+=1

		colIndex = 0
		for rowT in self.array.T:
			if (not otherLetter(letter) in rowT) and twoOccurences(letter, rowT):
				# print("here and colindix: ", colIndex, " and rowT: ", rowT)
				# return True
				targetRow = self.findWinningSpot(letter, rowT)
				return targetRow, colIndex
			colIndex+=1

		# diags = [[self.array[0][0], self.array[1][1], self.array[2][2]]]
		# for diag in 

		# Haven't checked diagonals yet
		return None

	def findWinningSpot(self, letter, row):
		i=0
		for possibility in row:
			if not possibility:		# this actually means "if we found the one"
				return i
			i+=1

def twoOccurences(letter, row):
	countOccurences = 0
	for possibility in row:
		if possibility == letter:
			countOccurences += 1
	if countOccurences == 2:
		return True

def otherLetter(letter):
	if letter == "X":
		return "O"
	elif letter == "O":
		return "X"
	else: raise Exception("Invalid letter!")

def main():
	print("Welcome to TicTacToe AI!")

	ourBoard = Board(3)
	print(pd.DataFrame(np.matrix(ourBoard.array)))

	print("I'll go first:")
	ourBoard.putX(1,1)

	print(pd.DataFrame(np.matrix(ourBoard.array)))
	print("What's your move?")
	coords = input("Input comma seprated coords: ")
	tupleCoords = tuple(coords.split(","))
	print("Putting a O at ", tupleCoords, "\n")
	ourBoard.putO(int(tupleCoords[1]),int(tupleCoords[0]))
	print(pd.DataFrame(np.matrix(ourBoard.array)))

	gameOver = False
	while not gameOver:
		print("My turn")
		chosenRow, chosenCol = ourBoard.chooseBestXSpot()
		ourBoard.putX(chosenCol,chosenRow)

		print(pd.DataFrame(np.matrix(ourBoard.array)))
		ourBoard.checkWinConditions("X")

		if not ourBoard.emptySpots():
			print("Looks like it's a draw!")
			exit()

		print("What's your move?")
		coords = input("Input comma seprated coords: ")
		tupleCoords = tuple(coords.split(","))
		print("Putting a O at ", tupleCoords, "\n")
		ourBoard.putO(int(tupleCoords[1]),int(tupleCoords[0]))
		print(pd.DataFrame(np.matrix(ourBoard.array)))

		ourBoard.checkWinConditions("O")

if __name__ == '__main__':
	main()