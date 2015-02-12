class Customer():
	''' A customor with a name and amount of money./
		Customer can buy a car if he/she has enough money./
		Customer can check to see the list of bicycles that he/she can buy.'''
	def __init__(self, name, money):
		self.name = name
		self.money = money

	def available_bikes(self, margin_str, bike_inst):
		''' Returns list of bikes(ava_bikes) that a customer can buy.
			'margin_str, bike_inst' from Bike_shop.
			'margin_str' is derectly from the Bike_shop class and we use margin.
			'bike_inst' is a list of Bicycle instances from Bicycle class so we refer
			to the original price  and also their name in the Bicycle class.
			margin is the percent of money that the store will add to the oringinal price of a bike.
		'''
		bike_list= []
		for bike in bike_inst:
			if self.money > (bike.org_price + (margin_str * bike.org_price)) :
				bike_list.append(bike.name)
		print ' %s can buy these bikes : %s' %(self.name, bike_list)

	def buy_bike(self, selected_bike_inst, margin_str):
		sellprice = (selected_bike_inst.org_price + (margin_str * selected_bike_inst.org_price))
		if self.money > sellprice:
			self.money -= sellprice
			print ' %s bought %s and now she has %s $ left over' %(self.name, selected_bike_inst.name, self.money)

			return 1
#	def report(self):

class Bicycle():
	''' defining bicycles. it returns nothing:)!'''
	def __init__(self, name, weight, original_price):
		self.name = name
		self.weight= weight
		self.org_price = original_price


class Bike_shop():
	def __init__(self, name, margin, *bikes_inst):
		''' each shop will have a name, margin(percent of monet that company addes to the original/
			sell price and list of bike instances)'''
		self.name = name
		self.margin = margin
		
		self.bike = [] # explanation 1!
		for b in bikes_inst:
			self.bike.append(b)
	def sell(self, cust_inst, bike_inst):

		if (cust_inst.buy_bike(bike_inst, self.margin)) == 1:
		#sellprice = (bike_inst.org_price + (self.margin * bike_inst.org_price))
		#if cust_inst.money > sellprice:
			self.bike.remove(bike_inst)
			print 'list of remaining cars in the shop:'
			for bike in self.bike:
				print bike.name
	def report(self):
		print "The grand profit for the %s is %d" % (self.name, self.profit)			

	def inventory(self):
		for bike in self.bikes:
			print (bike.name,int(bike.price + (self.margin * bike.price)))


c1 = Customer('mary', 300)

B1=Bicycle('b1', 1, 100)
B2=Bicycle('b2', 2, 400)
B3=Bicycle('b3', 3, 800)

shop = Bike_shop('shop1', 0.20, B1,B2,B3)

c1.available_bikes(shop.margin, shop.bike)
c1.buy_bike(B1, shop.margin)
shop.sell(c1, B1)
