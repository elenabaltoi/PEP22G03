"""
A shop needs an iterable object to keep track of product expiration dates.
Each product in the shop will have a string name, datetime expiration date and quantity
Iterating the object will return all products in the shop ordered by expiration date
1) 40p: Definition
    a) 10p: Basic class structure of objects
    b) 10p: Basic class structure of iterator
    b) 10p: Method to add product to the shop
    c) 10p: Method to decrease quantity and remove product
2) 40p: Execution:
    a) 10p: Create instance of your shop
    b) 10p: Add products:
        - Banana, 1 Aug 2022, 100
        - Orange, 2 Aug 2022, 200
        - Orange, 3 Aug 2022, 50
    c) 10p: Remove products
        - Orange, 10
        - Banana, 50
    d) 10p: Iterate the created object.
3) 20p: Documenting:
   a) 5p: type hints for arguments
   a) 5p: module documentation
   b) 5p: class documentation for all classes
   c) 5p: method documentation for all methods
"""

import time
import datetime

class Shop():
    """" products class """

    products={}

    def __init__(self, product: str):
        self.product = product

    def __iter__(self):
        return ShopIteratorterator(self.product)

    def add_product (self, product, exp_date):
        """" adding products method """
        day, month, year = exp_date.split("/")
        self.products[product].append(product)



class ShopIterator():
    """"iterator class"""


    def __init__(self, products: dict):
        pass


    def __iter__(self):
        return self

    def __next__(self):
        pass

p = Shop(products)
p.add_product({"Banana":{'1 Aug 2022' : 100}})
print(p)