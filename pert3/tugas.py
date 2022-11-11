from abc import ABC, abstractmethod
from itertools import product
class abstrak:
    @abstractmethod
    def get_ProductID(self): #Fungsi Getter
        return self.get_ProductID
    @abstractmethod
    def get_ProductName(self): #Fungsi Getter
        return self.get_ProductName
    @abstractmethod
    def get_Price(self): #Fungsi Getter
        return self.Price
    @abstractmethod
    def get_Quantity(self): #Fungsi Getter
        return self.Quantity
    @abstractmethod
    def set_Price(self, new_Price): #Fungsi Setter
        self.Price = new_Price
    @abstractmethod
    def set_Quantity(self, new_Quantity): #Fungsi Setter
        self.Quantity = new_Quantity

class product:
        def __init__(self, ProductID, ProductName, Price, Quantity): #Konstruktor
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.Price = Price
        self.Quantity = Quantity

Product1 = product(1,'Indomie',3000,100) #Atribut
print("ProductID: {}".format(Product1.get_ProductID()))
print("Product Name: {}".format(Product1.get_ProductName()))
print("Price: {}".format(Product1.get_Price()))
print("Quantity: {}".format(Product1.get_Quantity()))
Product1.set_Price(3500)
Product1.set_Quantity(200)
print("New Price: {}".format(Product1.get_Price()))
print("Updated Quantity: {}".format(Product1.get_Quantity()))



