"""
You're challenge for today is to create a random password generator! 
For extra credit, allow the user to specify the amount of passwords to generate.
For even more extra credit, allow the user to specify the length of the strings he wants to generate!
"""

import random
import string
from string import digits

def generate_passwords(numPass = 1, passLen = 7):
  for i in range(numPass):
    password = []
    for j in range(passLen):
      randomChar = random.choice(string.letters + digits)
      password.append(randomChar)
    print ''.join(password)

generate_passwords(15, 15)
