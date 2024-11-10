from produkty  import  *  ### zaimportoanie produktów za pomocą gwiazdki

class Cart:
    def __init__(self):
        self.__productList = []
        self.__cartValue = 0    ###wartość koszyka

    def addProduct(self, product): ### możliwość dodawania produktów
        #if isinstance(product, Phone) or isinstance(product, TV): ### isinstance dostarcza informacji czy cos jest instancja czegoś, jako pierwszy argument przekazuje się to co chce sie sp
         if isinstance(product, Product):
            if product not in self.__productList:  ### sprawdzam czy ten produkt jest już na liście
                self.__productList.append(product)                                ### użytkownik może dodać tylko jeden produkt do listy np. towar jest deficytowy
                self.calculateCart()    ### metoda wywołan podczas dodawania produktu do koszyka




    def calculateCart(self):   ### metoda podsumwania koszyka
       self.__cartValue = 0 ### wartość początkowa, aby uniknąć zawyżenia koszyka tyle razy ile będzie wywołane calculateCart
       for el in self.__productList:
           self.__cartValue += el.price  ### wszystkie kalkulacje powinna być względem początkowej wartości która wynosi zero






    def __str__(self):  ### metodsa która wyświetli informacje o koszyku
        strData = "\nCart Info, products list "
        for el in self.__productList:    ### za pomocą pętli przechodzimy  po wszystkich elementach
            strData += "\n - " + str(el.name) + " " + str(el.price)
        strData += "\n Cart value: " + str(self.__cartValue)
        return strData
