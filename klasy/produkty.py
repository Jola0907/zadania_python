## koszyk zakupów z użyciem klas, w folderze CArt kilka plików:
## nasz plik czyli koszyk
## nasze produkty
## główny plik programu
## plik Product czyli nzasze produkty , główna klasa konstruktor, name, price

class Product:  #główna klasa
    def __init__(self, name, price):  #konstruktor
        self.name = name
        self.price = price


    def __str__(self):  #metoda str, gdy użyje funkcji print wyświetli się opis produktu
        return str(self.name) + " " + str(self.price) #skonwertowane na łańcuch znaków


class Phone(Product): ####klasa która rozszerza klase produkt
    def __init__(self, name, price, color):
        Product.__init__(self, name, price)  ####WYWOŁANIE KONSTRUKTORA KLASY PRODUCT
        self.color = color


    def __str__(self):
        return super().__str__() + " " + str(self.color)   ###odziedziczyć po klasie Product metode str przy pomocy "super"





phone1 = Phone("Phone X", 1000, "RED")
print(phone1)

phone2 = Phone("Iphone X", 3000, "Black")
print(phone2)

phone3 = Phone("Huawei", 400, "Black")
print(phone3)

class TV(Product):  #rozszerzamy klase Prpduct
    def __init__(self, name, price, screenSize):
        super().__init__(name, price)         ###przy pomocy super odwołać się można do nadrzędnej klasy, a self jest automatycznie przepisane
        self.screenSize = screenSize
    def __str__(self):
        return super().__str__() + " " + str(self.screenSize)  ###za pomocą "super" odwołanie do nadrzędnej wersji str


tv1 = TV("TV Y", 2000, 65)
print(tv1)
tv2 = TV(" TV X", 4000, 75)
print(tv2)
tv3 = TV(" TV W", 7000, 90)
print(tv3)