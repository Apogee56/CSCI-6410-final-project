import sys
from Graph import Graph
from Bee import Bee

#RUNTIME PARAMETERS
MFE = 20000
limit = 200
n_e = 20

#Initial function evaluations
feval = 0

# reading in the graph and initializing the graph
filename = sys.argv[1]
f = open(filename, "r")
v = int(f.readline())
e = int(f.readline())
g = Graph(v, e)
for i in range(0, g.enum):
	line = f.readline()
	g.elist.append(list(line.split(" ")))
	g.elist[-1][0] = float(g.elist[-1][0])
	g.elist[-1][1] = int(g.elist[-1][1])
	g.elist[-1][2] = int(g.elist[-1][2])

#FUNCTION TESTERS
#print(g.weight())
#print(g.subGraph([1,0,1,0,1,0,1,0,1]).elist)
#print(sorted(g.elist))
#x = g.kruskal()
#print(x.connected())
#print(x.elist)
#print(g.cycDetect(g.elist))
#b = Bee(limit)
#print(b.type)
#b.randomfood(g)
#b.mutatefood(g)
#b.evaluate(g)

beelist = []

#initializing food source/employed bees
for i in range(0, n_e):
	tempbee = Bee(limit)
	tempbee.randomfood(g)
	feval += 1
	beelist.append(tempbee)

#Getting the kruskal graph and the weight of the graph, since the
#weight is a termination condition
x = g.kruskal()
krusweight = x.weight()
print ("Kruskal's Algorithm: " + str(krusweight))

#The list for storing the best foods at the end of each round.
bestfoods = []

while (feval < MFE and (bestfoods == [] or bestfoods[0][0] != krusweight)):
	#employed bee stage
	for i in range(0, len(beelist)):
		#print ("TIME" + str(feval))
		beelist[i].mutatefood(g)
		beelist[i].evaluate(g)
		feval += 1
	#Scout bee stage
	for i in range(0, len(beelist)):
		beelist[i].limitcheck(g)
	#storing the best solution
	beelist.sort(key=lambda bee: bee.foodfitness)
	for i in beelist:
		if i.foodfitness > -1:
			if (i.foodfitness, i.foodsource) not in bestfoods:
				bestfoods.append((i.foodfitness, i.foodsource))
	bestfoods.sort()

#printing the n_e best paths
for i in range(0, n_e):
	print(bestfoods[i])
	if (i+1 == len(bestfoods)):
		break
	