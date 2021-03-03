# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.
# Other abilities of a Circle instance: 
# * Compute the circle’s area 
# * Print the circle and get something nice 
# * Be able to add two circles together 
# * Be able to compare two circles to see which is bigger 
# * Be able to compare to see if there are equal 
# * Be able to put them in a list and sort them
import math

class Circle():
    def __init__(self, radius):
        self.radius = radius
    
        
    def area(self):
        area = math.pi * (self.radius**2)
        return area

    def diameter(self):
        diameter = math.pi * (self.radius * 2)
        return diameter

    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False
    
    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False
    
    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

   

