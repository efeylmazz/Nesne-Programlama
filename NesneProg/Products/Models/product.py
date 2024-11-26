from datetime import datetime

class Product:
    def __init__(self, name="Default", price=0, quantity=1, brand=None):
        print(f"An instance with name {name} has been derived from Product class.")
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__brand = brand
        
        creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Created Date: {creation_date}")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value
    
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self.__price = value
    

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            print("Quantity cannot be negative!")
        else:
            self.__quantity = value

    def get_total_price(self):
        return self.__price * self.__quantity

    
    def __str__(self):
        total_price = self.get_total_price() 
        return (f"Product: {self.__name}\n"
                f"Unit Price: ${self.__price:.2f}\n"
                f"Quantity: {self.__quantity}\n"
                f"Brand: {self.__brand if self.__brand else 'No Brand'}\n"
                f"Total Price: ${total_price:.2f}")
       

