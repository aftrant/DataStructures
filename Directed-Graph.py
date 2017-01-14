class Currency(object):
	def __init__(self, name):
		self.name = name
		self.rates = []

	def getName(self):
		return self.name

	def getRates(self):
		return self.rates

	def addRateEdge(self, r):
		self.rates.append(r)

	def addRate(self, currency, weight=0)
		e = Edge(currency, weight)
		self.rates.append(e)


class Edge(object):
	def __init__(self, currency, rate=0):
		self.currency = currency
		self.exchange = rate

	def getCurrency(self):
		return self.currency

	def getExchange(self):
		return self.exchange

	def setExchange(self, exchange):
		self.exchange = exchange



