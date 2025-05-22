# CONSTRUCTOR - Here __init__ is a constructor when object is created from the class it automatically calls
# SELF -  self is like defining the current object name here object is DETAIL so - 
# self = detail - self.name means detail.name

#self defines current object & Constructor It runs automatically when you create an object from a class.
# instead of calling it manually , using constructor it calls the function automatically
class student:
    def __init__(self): 
        self.name = "Mukund"
        self.regi = "123"
    def display(self):
        print("Name = ", self.name)
        print("Register = ", self.regi)

detail = student() # Automatically calls
detail.name = "Mukund"
detail .regi = "3070172"
detail.display()

        