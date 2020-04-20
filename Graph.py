import queue

class Graph:
	
	elist = []
	vlist = []
	
	def __init__(self,v,e = 0):
		self.vnum = v
		self.enum = e
		
	def weight(self):
		sum = 0
		for i in self.elist:
			sum = sum + i[0]
		return sum
		
	def subGraph(self, encoding):
		
		numedges = 0
		numverts = self.vnum
		newelist = []
		
		for i in range(0, len(encoding)):
			if encoding[i] == 1:
				numedges += 1
				newelist.append(self.elist[i])
				
		res = Graph(numverts, numedges)
		res.elist = newelist
		
		return res
		
	def buildAdj(self):
		adjList = [[]]
		for i in range(1, self.vnum + 1):
			temp = []
			for e in self.elist:
				if e[1] == i:
					temp.append(e[2])
				elif e[2] == i:
					temp.append(e[1])
			adjList.append(temp)
		self.adj = adjList
		
	def connected(self):
	
		self.buildAdj()
		explored = []
		q = queue.LifoQueue(self.vnum + 2)
		q.put(1)
		
		while (not q.empty()):
			curver = q.get()
			curadj = self.adj[curver]
			if curver not in explored:
				explored.append(curver)
			for x in curadj:
				if x not in explored:
					q.put(x)		
		if len(explored) == self.vnum:
			return True
		else:
			return False
			
	def kruskal(self):
		connected = []
		edges = sorted(self.elist)
		newelist = []
		
		while len(newelist) < self.vnum - 1 and len(edges) > 0:
			edge = edges[0]
			del edges[0]
			newelist.append(edge)
			flag = self.cycDetect(newelist)
			if(flag == 1):
				del newelist[-1]
			if(flag == 0):
				if edge[1] not in connected:
					connected.append(edge[1])
				if edge[2] not in connected:
					connected.append(edge[2])
		res = Graph(self.vnum,len(newelist))
		res.elist = newelist
		return res
				
	def cycDetect(self, edges):
		
		y = Graph(self.vnum, self.enum)
		y.elist = edges
		y.buildAdj()
		unexplored = list(range(1, self.vnum + 1))
		q = queue.LifoQueue(self.vnum + 2)			
		
		
		while len(unexplored) > 0:	
			q.put((-1,unexplored[0]))
			while (not q.empty()):
				curver = q.get()
				if curver[1] in unexplored:
					unexplored.remove(curver[1])
				curadj = y.adj[curver[1]]
				for x in curadj:
					if x in unexplored:
						q.put((curver[1],x))
					elif x != curver[0]:
						return True
		return False
		
		
	
				
		
		