import sys

tile_open = 0
tile_mountain = 1
tile_snake = 2
tile_barn = 3

discount = 0.9
rew_mountain = -1
rew_snake = -2
rew_barn = 1
rew_apple = 50

class node:
	def _init_(self, parent, location):
		self.parent = parent
		self.location = location
		self.f = none
		self.g = none
		self.h = none
	
def probability():
	percentage = randint(1, 100)
	if percentage <= 10:
		#goes left of intended move
		return (percentage * .01)
	if percentage >= 90:
		#goes right of intended move
		return (percentage * .01)
	else:
		#goes forward of intended move
		return (percentage * .01)

def adjacent(row, col, maxRow, maxCol):
	neighbor = []
	if col >= 0:
		if (col - 1) >= 0:
			neighbor.append(row, (col - 1))
		if (col + 1) < maxCol:
			neighbor.append(row, (col + 1))
	if row >= 0:
		if (row - 1) >= 0:
			neighbor.append((row - 1), col)
		if (row + 1) < maxRow:
			neighbor.append((row + 1), col)
	return neighbor
	
def utilityEval(row, col, world):
	north = ((0.8 * rewardForward) + (0.1 * rewardLeft) + (0.1 * rewardRight))
	south = ((0.8 * rewardForward) + (0.1 * rewardLeft) + (0.1 * rewardRight))
	east = ((0.8 * rewardForward) + (0.1 * rewardLeft) + (0.1 * rewardRight))
	west = ((0.8 * rewardForward) + (0.1 * rewardLeft) + (0.1 * rewardRight))
	finalResult = [north, south, east, west]
	return finalResult

def markov(start, end, world):
	listClosed = []
	listOpen = []
	
	rootNode.h = probability.chosen(start, goal)
	rootNode.g = 0
	rootNode.f = rootNode.h
	listOpen.append(start)
	while len(listOpen) != 0:
		currentNode = minCost(listOpen)
		if currentNode == end:
			return currentNode
			listClosed.append(currentNode)
			for nextLocation in world[currentNode.location]:
				nextNode = node(currentNode, nextLocation)
				nextNode.g = currentNode.g + cost
				nextNode.h = probability.chosen(nextNode.location, goal)
				nextNode.f = nextNode.g + nextNode.h
				if nextNode.location == goal:
					listClosed.append(nextNode)
					return (nextNode, len(listClosed))
	return None
		
def main(argv):
	world = open(filename)
	return None
