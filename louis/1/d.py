"""
[difficult] challenge #1
we all know the classic "guessing game" with higher or lower prompts. lets do a role reversal; you create a program that will guess numbers between 1-100, and respond appropriately based on whether users say that the number is too high or too low. Try to make a program that can guess your number based on user input and great code!
"""

import random

lower = 0
upper = 101
answer = ''

while answer != 'yes':
  guess = random.randrange(lower, upper)
  answer = raw_input("Is %s your number? " % (guess));
  if (answer == 'too high'):
    upper = guess
  elif (answer == 'too low'):
    lower = guess

print "heh, i knew I'd get it.."
