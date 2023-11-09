#Namirah
#11/8/2023

#Given the following code with the Python Class ‘car’:

class car:
    def __init__(self, model, year, color, type, manufacture):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacture = manufacture
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    def get_color(self):
        return self.color
    def get_type(self):
        return self.type
    def get_manufacture (self):
        return self.manufacture
    def fullspecs(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color + ' ' + self.type + ' ' + self.manufacture


car1 = car("Sports", 2012, "Blue", "suv", "honda")
car2 = car("Sedan", 2020, "Black", "sedan", "kia")

print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())

#Attributes and methods are two fundamental components that define the behavior and characteristics of objects created from that class. Attributes are variables associated with an object and represent its characteristics or state. They store data and can be accessed directly. Methods, on the other hand, are functions defined within a class that describe the actions an object can perform. They are used to manipulate the object's attributes or provide functionality. Methods are called using parentheses and may take arguments, while attributes are accessed without parentheses. In essence, attributes represent data, while methods represent actions or behavior within a class.