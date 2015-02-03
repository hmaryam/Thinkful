
class Customer():
	def __init__(self, name, fund):
		self.name= name
		self.fund = fund
		self.bicycle = None

	def buyBicycle(self,model, sellPrice):
		if(sellPrice > self.fund):
			print " You do not have enough money..."
			return 0
		else:
			self.bicycle = model
			self.fund -= sellPrice
			print "Left over for %s: $%s" % (self.name, self.fund)
			return 1
	def affordable(self, margin, bicycles):
		bike_list= []
		for bike in bicycles:
			if ( int(bike.price + (margin * bike.price)) < self.fund):
				bike_list.append(bike.name)
		print self.name, bike_list

class Bicycle(object):
	def __init__(self, name, weight, price):
		self.name = name
		self.weight = weight
		self.price = price
	def description(self):
		print "The model is %s and its weight %s.The price is %d" % (name, weight,price)



class BikeShop(object):

	def __init__(self, name, margin, *bicycles):
		self.name= name
		self.margin = margin
		self.profit = 0
		self.bikes = []
		for bike in bicycles:
			self.bikes.append(bike)

	#New
	def sell(self,customer, bicycle):
		sellPrice = int(bicycle.price + (self.margin * bicycle.price))
		
		if(customer.buyBicycle(bicycle.name, sellPrice) == 1):
			self.bikes.remove(bicycle)
			self.profit += int(self.margin * bicycle.price)
			self.inventory()
			self.report()


	def report(self):
		print "The grand profit for the %s is %d" % (self.name, self.profit)

	def inventory(self):
		for bike in self.bikes:
			print (bike.name,int(bike.price + (self.margin * bike.price)))
