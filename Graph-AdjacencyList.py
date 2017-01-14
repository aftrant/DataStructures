class node(object):
	def __init__(self, name, weight=0):
		self.name = name
		self.pop = weight
		self.edges = []  # roads

	def getName(self):
		return self.name
	
	def getPopulation(self):
		return self.pop

	def getEdges(self):  # getCities()
		return self.edges

	def addNeighborEdge(self, e):  # addNeighborRoad()
		self.edges.append(e)

	def addNeighborNode(self, node, weight=0):
		e = edge(node, weight)
		self.edges.append(e)


class edge(object):
	def __init__(self, node, weight=0):
		self.node = node
		self.weight = weight

	def getNode(self):
		return self.node

	def getWeight(self):
		return self.weight


def addEdge(name1, name2, weight=0):  # addRoad(name1, name2, weight=0)
	edge1 = edge(name2, weight)
	edge2 = edge(name1, weight)
	for city in cities:
		if city.getName() == name1:
			city.addNeighborEdge(edge1)
		if city.getName() == name2:
			city.addNeighborEdge(edge2)

def addEdge2(name1, name2, weight=0): 
	for city in cities:
		if city.getName() == name1:
			city.addNeighborNode(name2, weight)
		if city.getName() == name2:
			city.addNeighborNode(name1, weight)


cities = []  # nodes = []

city = node('Rivertown', 100)
cities.append(city)
city = node('Brookside', 1500)
cities.append(city)
city = node('Hillsview', 500)
cities.append(city)
city = node('Forrest City', 800)
cities.append(city)
city = node('Lakeside', 1100)
cities.append(city)

addEdge('Rivertown', 'Brookside', 100)
addEdge('Rivertown', 'Hillsview', 50)
addEdge('Brookside', 'Hillsview', 130)
addEdge('Hillsview', 'Forrest City', 40)
addEdge('Forrest City', 'Lakeside', 80)

print cities

for city in cities:
	print 'Neighbors of ' + city.getName()
	roads = city.getEdges()
	for road in roads:
		print '     ', road.getNode(), 'at a distance', road.getWeight()
