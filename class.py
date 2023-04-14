'''
Exercise 1: Turn the shopping cart program from yesterday into an object-oriented program
'''

class Cart:
    def __init__(self, name:str):
        self.cart = {}
        self.name = name

    def add(self, item, quantity:int):
        item = item.upper()
        self.cart[item] = self.cart.get(item, 0) + quantity

    def remove(self, item, quantity:int):
        item = item.upper()
        if item not in self.cart:
            return "This item does not exist in your cart."
        self.cart[item] = self.cart.get(item, 0) - quantity
        if self.cart[item] == 0:
            del self.cart[item]

    def show(self):
        if self.cart:
            print(f"\n{self.name}'s SHOPPING CART")
            for k, v in self.cart.items():
                print(f"Item: {k} - Quantity: {v}")
        else:
            print("Your cart is currently empty")

my_cart = Cart("YY")
my_cart.add("Cookies", 2)
my_cart.add("water", 5)
my_cart.remove("water", 3)
my_cart.show()

'''
Exercise 2 - Create a class 'Ford' that inherits from 'Car' class and initialize it as a Blue Ford Explorer with 4 wheels using the super() method, add a method to car which prints 'this is a car' and create an overriding method in class Ford that prints the information on the car
'''

class Car:
    def __init__(self, wheels, doors):
        self.wheels = wheels
        self.doors = doors

    def statement(self):
        print(f"This is a {self.wheel} wheeled, {self.door} door car.")


class Ford(Car):
    def __init__(self, color, model, make, year, wheels, doors):
        super().__init__(wheels, doors)
        self.color = color
        self.make = make
        self.model = model
        self.year = year

    def statement(self):
        return (f"This is a {self.year} {self.color} {self.make} {self.model}.")

my_car = Ford("Blue", "Explorer", "Ford", "2023", 4, 4)
print(my_car.wheels)
print(my_car.statement())
