"""
[easy] challenge #2
Hello, coders! An important part of programming is being able to apply your programs, so your challenge for today is to create a calculator application that has use in your life. It might be an interest calculator, or it might be something that you can use in the classroom. For example, if you were in physics class, you might want to make a F = M * A calc.

EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to calculate F = M * A, but also A = F/M, and M = F/A!
"""

import math
from math import pi

def calcArea ():
  radius = float(raw_input("Enter radius of the circle: "))
  return "The area of the circle is %s\n" % (pi * radius**2)

def calcCircumference ():
  radius = float(raw_input("Enter radius of the circle: "))
  return "The circumference of the circle is %s" % (2 * pi * radius)

def calcVolume ():
  radius = float(raw_input("Enter radius of the circle: "))
  return "The volume of the sphere is %s" % ((4.0 / 3.0) * pi * radius**3)

def calcRadius ():
  term = raw_input("Calculate radius from 'area', 'circumference', or 'volume': ")
  if (term == 'area'):
    area = float(raw_input("What is the area of the circle? "))
    return "The radius of the circle is %s" % (math.sqrt(area / pi))
  elif (term == 'circumference'):
    circumference = float(raw_input("What is the circumference of the circle? "))
    return "The radius of the circle is %s" % (circumference / (2 * pi))
  elif (term == 'volume'):
    volume = float(raw_input("What is the volume of the sphere? "))
    return "The radius of the circle is %s" % (math.pow(((3 * volume) / (4 * pi)), float(1)/3))
  else:
    print pickAgain()

def pickAgain ():
  return "That choice is not supported.  Please choose again.\n"

def quit ():
  return "bye!"

# Initialize variables
choice = ''
circle = {
          'area' : calcArea,
          'circumference' : calcCircumference,
          'volume' : calcVolume,
          'radius' : calcRadius,
          'quit'   : quit
         }

print "Welcome to Circle calculator!\n"

while choice != 'quit':
  choice = raw_input("Type 'area', 'circumference', or 'volume'.  You can also type 'radius' to calculate it from a given area, circumference, or volume.  Type 'quit' to exit: ");
  print circle.get(choice, pickAgain)()
