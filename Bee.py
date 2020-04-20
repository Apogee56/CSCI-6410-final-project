import queue
import random
import Graph
class Bee:
	
	foodsource = []
	foodfitness = -1
	tempfood = []
	tempfitness = -1
	lastimproved = 0
	limit = 5
	
	
	def __init__(self, lim):
		
		self.limit = lim
		
	#This method selects a random food source and calculates its fitness
	def randomfood(self, basegraph):
		food = [0] * basegraph.enum
		foodindices = list(range(0, basegraph.enum))
		count = 0
		while (count < basegraph.vnum-1):
			tempind = random.choice(foodindices)
			foodindices.remove(tempind)
			count += 1
			food[tempind] = 1
		self.foodsource = food
		self.foodfit(basegraph)
	
	#calculates the food fitness for self's foodsource
	def foodfit(self, basegraph):
		#building graph for food encoding
		foodsub = basegraph.subGraph(self.foodsource)
		
		#determining fitness
		if not foodsub.connected():
			self.foodfitness = -1
		else:
			self.foodfitness = foodsub.weight()
		
	#calculates the food fitness for self's tempfood
	def tempfit(self, basegraph):
		
		if self.tempfood != []:
			#building graph for food encoding
			tempsub = basegraph.subGraph(self.tempfood)
			
			#determining fitness
			if not tempsub.connected():
				self.tempfitness = -1
			else:
				self.tempfitness = tempsub.weight()
			
			
	#This method initializes the tempfood by switching a zero and 1
	def mutatefood(self, basegraph):
		
		#retrieves the indices where 1's and 0's appear in the foodsource
		foodindices0 = list(range(0, basegraph.enum))
		foodindices1 = []
		for i in range(0, basegraph.enum):
			if self.foodsource[i] == 1:
				foodindices1.append(i)
				foodindices0.remove(i)
		
		#mutating the food by switching a 1 and a zero.
		newfood = self.foodsource.copy()
		temp0 = random.choice(foodindices0)
		temp1 = random.choice(foodindices1)
		newfood[temp0] = 1
		newfood[temp1] = 0
		self.tempfood = newfood
		
		self.tempfit(basegraph)
		
	def evaluate(self, basegraph):
		
		#replacing food if necessary
		if self.tempfitness > 0:
			if ((self.foodfitness < self.tempfitness) or (self.foodfitness == -1)):
				self.foodfitness = self.tempfitness
				self.foodsource = self.tempfood.copy()
			else:
				self.lastimproved += 1
		else:
			self.lastimproved += 1
			
		#erasing the temporary food when done
		self.tempfood = []
		self.tempfitness = -1
			
	def limitcheck(self, basegraph):
		if (self.lastimproved >= self.limit):
			self.randomfood(basegraph)
		
			
			
		
		