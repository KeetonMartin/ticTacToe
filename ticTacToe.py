#Author: Keeton Martin
import numpy as np
import pandas as pd

class Board():
	"""docstring for Board"""
	def __init__(self, size):
		self.size = size

		#Create a size x size empty array
		self.array = np.empty((3,3), dtype=str)

	def insertAtIndex(self, i, j, letter):
		self.array[i][j] = letter

	def putX(self, howManyFromLeft, howManyFromTop):
		# print(self)
		self.insertAtIndex(howManyFromTop, howManyFromLeft, "X")
		# print(self)
		self.checkWinConditions("X")

	def putO(self, howManyFromLeft, howManyFromTop):
		# print(self)
		self.insertAtIndex(howManyFromTop, howManyFromLeft, "O")
		# print(self)
		self.checkWinConditions("O")

	def __str__(self):
		return str(self.array)

	def checkWinConditions(self, letter):
		if self.checkWonOnRow(letter): #or self.checkWonOnCol(letter) or self.checkWonOnDiag(letter):
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

	def checkWonOnCol(self):
		pass
		
	def checkWonOnDiag(self):
		pass

	def chooseBestXSpot(self):
		pass

	def playerCouldWin(self, letter):
		for row in self.array:
			if (not otherLetter(letter) in row) and twoOccurences(letter, row):
				ourBoard.findWinningSpot(letter, row)
		for rowT in self.array.T:
			if (not otherLetter(letter) in row) and twoOccurences(letter, row):

	def findWinningSpot(self, letter, row):
		for possibility in row:
			if possibility = " ":


def twoOccurences(letter, row):
	countOccurences = 0
	for possibility in row:
		if possibility == letter:
			count += 1
	if countOccurences == 2

def otherLetter(letter):
	if letter == "X":
		return "O"
	elif letter == "O":
		return "X"
	else: error("Invalid letter!")

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
		chosenSpot = ourBoard.chooseBestXSpot()
		ourBoard.putX(int(tupleCoords[1]),int(tupleCoords[0]))

		ourBoard.checkWinConditions("X")

		print(pd.DataFrame(np.matrix(ourBoard.array)))
		print("What's your move?")
		coords = input("Input comma seprated coords: ")
		tupleCoords = tuple(coords.split(","))
		print("Putting a O at ", tupleCoords, "\n")
		ourBoard.putO(int(tupleCoords[1]),int(tupleCoords[0]))
		print(pd.DataFrame(np.matrix(ourBoard.array)))

		ourBoard.checkWinConditions("O")

if __name__ == '__main__':
	main()