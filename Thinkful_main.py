import Thinkful_bicycle.py

c1 = Customer("John",200)
c2 = Customer("william", 500)
c3 = Customer("Brad", 1000)

B1 = Bicycle("B1",1,800)
B2 = Bicycle("B2",2,400)
B3 = Bicycle("B3",4,1200)
B4 = Bicycle("B4",2,100)
B5 = Bicycle("B5",1,600)
B6 = Bicycle("B6",2,50)

store = BikeShop("ShopName1", 0.20, B1,B2,B3,B4,B5,B6)
store.inventory()

c1.affordable(store.margin, store.bikes)
c2.affordable(store.margin, store.bikes)
c3.affordable(store.margin, store.bikes)



store.sell(c1,B6)
store.sell(c2,B2)
store.sell(c3,B5)

