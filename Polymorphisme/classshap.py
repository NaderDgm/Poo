'''class Vehicle:
    def description(self):
        return "This is a sayara."

class Car(Vehicle):
    def description(self):
        return "a car"

class Bicycle(Vehicle):
    def description(self):
        return "a bicycle."

car = Car()
bicycle = Bicycle()
print(car.description()) 
print(bicycle.description())



class Calculator:
    # def calculate(self, num1, num2):
    #     return num1 + num2

    # Surcharge #
    def calculate(self, num1, num2, num3=None):
        if num3 is None:
            return num1 + num2
        else:
            return num1 + num2 + num3

calc = Calculator()
print(calc.calculate(5, 3))
print(calc.calculate(5, 3, 2))'''
'''========================================================================================================'''
'''class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    #addition
    def __add__(self, other):
        return self.real + other.real , self.imag + other.imag
    
    #soustraction 
    def __sub__(self, other):
        return self.real - other.real, self.imag - other.imag
    
    #multiplication 
    def __mul__(self, other):
        real = self.imag * other.real 
        imag = self.imag * other.imag
        return real, imag

c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)

print(c1 + c2)  
print(c1.__add__(c2))

print(c1 - c2)
print(c1.__sub__(c2))

print(c1 * c2)
print(c1.__mul__(c2))'''