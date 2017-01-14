class node(object):
	def __init__(self, name, pop=0):
		self.name = name
		self.pop = pop

	def getName(self):
		return self.name

	def getPopulation(self):
		return self.pop

class edge(object):
	def __init__(self, node1, node2, weight=0):
		self.node1 = node1
		self.node2 = node2
		self.weight = weight

	def getNode1(self):
		return self.node1

	def getNode2(self):
		return self.node2

	def getNodes(self):
		return (self.node1, self.node2)

	def getWeight(self):
		return self.weight

def findPopulationByName(cities, roads, i):
	road = roads[i]
	pop1 = 0
	pop2 = 0
	for city in cities:
		if city.getName() == road.getNode1():
			pop1 = city.getPopulation()
		if city.getName() == road.getNode2():
			pop2 = city.getPopulation()
	total_population = pop1 + pop2
	return total_population

def findPopulationByIndex(cities, roads, i):
	road = roads[i]
	pop1 = cities[road.getNode1()].getPopulation()
	pop2 = cities[road.getNode2()].getPopulation()
	return pop1 + pop2

roads = []
cities = []

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

road = edge(0, 1, 100)  #road = edge('Rivertown', 'Brookeside', 100)
roads.append(road)
road = edge(0, 2, 50)  #road = edge('Rivertown', 'Hillsview', 50)
roads.append(road)
road = edge(2, 1, 130)  #road = edge('Hillsview', 'Brookside', 130)
roads.append(road)
road = edge(2, 3, 40)  #road = edge('Hillsview', 'Forrest City', 40)
roads.append(road)
road = edge(3, 4, 80)  #road = edge('Forrest City', 'Lakeside', 80) 
roads.append(road)

print roads
print cities
print findPopulationByIndex(cities, roads, 0)
