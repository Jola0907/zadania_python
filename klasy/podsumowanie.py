from zadania_python.klasy.cart import *  #### import Cart

#### podsumowanie zakupów

phone0 = Phone("Phone Z", 800, "black")  ### obiekt phone
tv0 = TV("TV Z", 4000, 65)

cart = Cart()  ### przekazanie obiektu do addProduct
cart.addProduct(phone0)
cart.addProduct(tv0)
cart.addProduct(tv1)
cart.addProduct(tv2)
cart.addProduct(tv3)
print(cart)